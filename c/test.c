SYSCALL_DEFINE2(magichostname, char __user *, name, int, len)
{
	int errno;
	char tmp[__NEW_UTS_LEN];

	if (len < 0 || len > __NEW_UTS_LEN)
		return -EINVAL;
	errno = -EFAULT;
	if (!copy_from_user(tmp, name, len)) {
		struct new_utsname *u;

		down_write(&uts_sem);
		u = utsname();
		memcpy(u->nodename, tmp, len);
		memset(u->nodename + len, 0, sizeof(u->nodename) - len);
		errno = 0;
		uts_proc_notify(UTS_PROC_HOSTNAME);
		up_write(&uts_sem);
	}
	return errno;
}


SYSCALL_DEFINE2(sethostname, char __user *, name, int, len)
{
	int errno;
	char tmp[__NEW_UTS_LEN]; //__NEW_UTS_LEN=64

	if (!ns_capable(current->nsproxy->uts_ns->user_ns, CAP_SYS_ADMIN))  //首先检查当前进程是否拥有CAP_SYS_ADMIN的授权
		return -EPERM;

	if (len < 0 || len > __NEW_UTS_LEN)
		return -EINVAL;
	errno = -EFAULT;
	if (!copy_from_user(tmp, name, len)) {  //copy_from_user将name指向的字符串从用户空间拷贝到内核空间，失败返回没有被拷贝的字节数，成功返回0
		struct new_utsname *u;

		down_write(&uts_sem);  //写者使用该函数来得到读写信号量sem，它会导致调用者睡眠，只能在进程上下文使用,用于获取Linux内核读写信号量中的写锁
		u = utsname();  //获取当前内核名称和其它信息，成功执行时，返回0。失败返回-1，errno被设为EFAULT，表示buf无效。
		memcpy(u->nodename, tmp, len);  //从源内存地址的起始位置开始拷贝若干个字节到目标内存地址中
		memset(u->nodename + len, 0, sizeof(u->nodename) - len);
		errno = 0;
		uts_proc_notify(UTS_PROC_HOSTNAME);  //使用UTS namespace隔离hostname
		up_write(&uts_sem);  //释放写锁
	}
	return errno;
}
