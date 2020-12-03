//1.背景图像，人物图像，怪兽图像等铺设
#include <graphics.h>
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#pragma comment(lib, "Winmm.lib")
#pragma comment(lib, "MSIMG32.LIB") //实现透明贴图

//定义全局变量
#define pictureWidth 8022 //背景图片宽度
#define pictureHigh 525   //背景图片高度
#define Width 1024        //画面宽度
#define High 525          //画面高度
#define roleWidth 39      //人物宽度
#define roleHigh 65       //人物高度
#define MonsterWidth 128  //怪兽宽度
#define MonsterWidth 128  //怪兽高度

int role_x, role_y;        //人物画布坐标
int real_x, real_y;        //人物实际坐标
int speed_x, speed_y;      //人物速度
int step_left, step_right; //人物行走脚步
int moveDeriction;         //人物行走判断1向左走，2向右走
int judgeOperate;          //人物是否可操作 0表示否 1表示能
int bk_x, bk_y;            //背景图片绘制坐标
int judgeJump;             //判断是否跳跃 0在地面，1为向上，2为向下
int flour;                 //地面高度
int jumpHigh, jumpHighTop; //人物跳跃限制

IMAGE img_bk;                                                                                                                  //背景画面
IMAGE img_role1r, img_role2r, img_role3r, img_role4r, img_role5r, img_role6r, img_role7r, img_role8r, img_role9r, img_role10r; //人物图片  向右
IMAGE img_role1l, img_role2l, img_role3l, img_role4l, img_role5l, img_role6l, img_role7l, img_role8l, img_role9l, img_role10l; //人物图片  向向左

struct kd // 空地下落
{
    int start_x, end_x;
};
kd KD[3]; // 空地

struct zc //可支撑物
{
    int start_x, end_x;
    int zc_high;
};
zc GD[6];    //管道
zc BKPH[26]; //不可破坏砖块

void startup() //数据初始化
{
    role_x = 100; //人物画布坐标
    role_y = 415;
    real_x = 100; //人物实际坐标
    real_y = 415;
    flour = 415;   //人物踩在地面时的高度
    speed_x = 5;   // 人物前进速度
    speed_y = 5;   //人物跳跃的速度
    step_left = 0; //人物行走图片循环
    step_right = 0;
    moveDeriction = 2; //人物行走判断1向左走，2向右走
    judgeOperate = 1;  //人物初始可以行走
    bk_x = 0;          //背景绘制坐标
    bk_y = 0;
    judgeJump = 0;               //判断是否跳跃 0表示否，1表示是
    jumpHigh = 0;                //人物跳跃高度为0
    jumpHighTop = High / 2 - 70; //人物跳跃极限高度

    KD[0].start_x = 2610; //空地坐标初始化
    KD[0].end_x = 2686;

    KD[1].start_x = 3255;
    KD[1].end_x = 3367;

    KD[2].start_x = 5790;
    KD[2].end_x = 5863;

    GD[0].start_x = 1062; //管道坐标初始化
    GD[0].end_x = 1135;
    GD[0].zc_high = 397;

    GD[1].start_x = 1438;
    GD[1].end_x = 1511;
    GD[1].zc_high = 359;

    GD[2].start_x = 1743;
    GD[2].end_x = 1811;
    GD[2].zc_high = 322;

    GD[3].start_x = 2160;
    GD[3].end_x = 2228;
    GD[3].zc_high = 322;

    GD[4].start_x = 6173;
    GD[4].end_x = 6240;
    GD[4].zc_high = 396;

    GD[5].start_x = 6777;
    GD[5].end_x = 6845;
    GD[5].zc_high = 396;

    BKPH[0].start_x = 5069; //不可破坏的砖块初始化
    BKPH[0].end_x = 5107;
    BKPH[0].zc_high = 434;

    BKPH[1].start_x = 5107;
    BKPH[1].end_x = 5146;
    BKPH[1].zc_high = 396;

    BKPH[2].start_x = 5146;
    BKPH[2].end_x = 5183;
    BKPH[2].zc_high = 359;

    BKPH[3].start_x = 5183;
    BKPH[3].end_x = 5222;
    BKPH[3].zc_high = 321;

    BKPH[4].start_x = 5297;
    BKPH[4].end_x = 5336;
    BKPH[4].zc_high = 321;

    BKPH[5].start_x = 5336;
    BKPH[5].end_x = 5373;
    BKPH[5].zc_high = 359;

    BKPH[6].start_x = 5373;
    BKPH[6].end_x = 5411;
    BKPH[6].zc_high = 396;

    BKPH[7].start_x = 5411;
    BKPH[7].end_x = 5449;
    BKPH[7].zc_high = 434;

    BKPH[8].start_x = 5599;
    BKPH[8].end_x = 5637;
    BKPH[8].zc_high = 434;

    BKPH[9].start_x = 5637;
    BKPH[9].end_x = 5676;
    BKPH[9].zc_high = 396;

    BKPH[10].start_x = 5676;
    BKPH[10].end_x = 5713;
    BKPH[10].zc_high = 359;

    BKPH[11].start_x = 5713;
    BKPH[11].end_x = 5751;
    BKPH[11].zc_high = 321;

    BKPH[12].start_x = 5751;
    BKPH[12].end_x = 5790;
    BKPH[12].zc_high = 321;

    BKPH[13].start_x = 5865;
    BKPH[13].end_x = 5904;
    BKPH[13].zc_high = 321;

    BKPH[14].start_x = 5904;
    BKPH[14].end_x = 5940;
    BKPH[14].zc_high = 359;

    BKPH[15].start_x = 5940;
    BKPH[15].end_x = 5979;
    BKPH[15].zc_high = 396;

    BKPH[16].start_x = 5979;
    BKPH[16].end_x = 6016;
    BKPH[16].zc_high = 434;

    BKPH[17].start_x = 6845;
    BKPH[17].end_x = 6885;
    BKPH[17].zc_high = 434;

    BKPH[18].start_x = 6885;
    BKPH[18].end_x = 6923;
    BKPH[18].zc_high = 396;

    BKPH[19].start_x = 6923;
    BKPH[19].end_x = 6961;
    BKPH[19].zc_high = 359;

    BKPH[20].start_x = 6961;
    BKPH[20].end_x = 7001;
    BKPH[20].zc_high = 321;

    BKPH[21].start_x = 7001;
    BKPH[21].end_x = 7038;
    BKPH[21].zc_high = 282;

    BKPH[22].start_x = 7038;
    BKPH[22].end_x = 7076;
    BKPH[22].zc_high = 245;

    BKPH[23].start_x = 7076;
    BKPH[23].end_x = 7113;
    BKPH[23].zc_high = 207;

    BKPH[24].start_x = 7113;
    BKPH[24].end_x = 7152;
    BKPH[24].zc_high = 169;

    BKPH[25].start_x = 7152;
    BKPH[25].end_x = 7190;
    BKPH[25].zc_high = 169;

    initgraph(Width, High);

    mciSendString("open Music\\back.mp3 alias bkmusic", NULL, 0, NULL); //背景音乐
    mciSendString("play bkmusic repeat", NULL, 0, NULL);                //循环播放

    loadimage(&img_bk, _T("Picture material\\背景图.png"));       //背景图片导入
    loadimage(&img_role1r, _T("Picture material\\人物1r.png"));   //人物图像导入
    loadimage(&img_role2r, _T("Picture material\\人物2r.png"));   //人物图像导入
    loadimage(&img_role3r, _T("Picture material\\人物3r.png"));   //人物图像导入
    loadimage(&img_role4r, _T("Picture material\\人物4r.png"));   //人物图像导入
    loadimage(&img_role5r, _T("Picture material\\人物5r.png"));   //人物图像导入    向右
    loadimage(&img_role6r, _T("Picture material\\人物6r.png"));   //人物图像导入
    loadimage(&img_role7r, _T("Picture material\\人物7r.png"));   //人物图像导入
    loadimage(&img_role8r, _T("Picture material\\人物8r.png"));   //人物图像导入
    loadimage(&img_role9r, _T("Picture material\\人物9r.png"));   //人物图像导入
    loadimage(&img_role10r, _T("Picture material\\人物10r.png")); //人物图像导入

    loadimage(&img_role1l, _T("Picture material\\人物1l.png"));   //人物图像导入
    loadimage(&img_role2l, _T("Picture material\\人物2l.png"));   //人物图像导入
    loadimage(&img_role3l, _T("Picture material\\人物3l.png"));   //人物图像导入
    loadimage(&img_role4l, _T("Picture material\\人物4l.png"));   //人物图像导入
    loadimage(&img_role5l, _T("Picture material\\人物5l.png"));   //人物图像导入    向左
    loadimage(&img_role6l, _T("Picture material\\人物6l.png"));   //人物图像导入
    loadimage(&img_role7l, _T("Picture material\\人物7l.png"));   //人物图像导入
    loadimage(&img_role8l, _T("Picture material\\人物8l.png"));   //人物图像导入
    loadimage(&img_role9l, _T("Picture material\\人物9l.png"));   //人物图像导入
    loadimage(&img_role10l, _T("Picture material\\人物10l.png")); //人物图像导入

    BeginBatchDraw();
}

// 半透明贴图函数
// 参数：
//		dstimg: 目标 IMAGE 对象指针。NULL 表示默认窗体
//		x, y:	目标贴图位置
//		srcimg: 源 IMAGE 对象指针。NULL 表示默认窗体
void transparentimage(IMAGE *dstimg, int x, int y, IMAGE *srcimg)
{
    HDC dstDC = GetImageHDC(dstimg);
    HDC srcDC = GetImageHDC(srcimg);
    int w = srcimg->getwidth();
    int h = srcimg->getheight();

    // 结构体的第三个成员表示额外的透明度，0 表示全透明，255 表示不透明。
    BLENDFUNCTION bf = {AC_SRC_OVER, 0, 255, AC_SRC_ALPHA};
    // 使用 Windows GDI 函数实现半透明位图
    AlphaBlend(dstDC, x, y, w, h, srcDC, 0, 0, w, h, bf);
}

void RoleWalk(int left, int right, int judge) //人物行走
{
    if (judge == 1)
    {
        switch (left)
        {
        case 0:
            transparentimage(NULL, role_x, role_y, &img_role1l);
            break;
        case 1:
            transparentimage(NULL, role_x, role_y, &img_role2l);
            break;
        case 2:
            transparentimage(NULL, role_x, role_y, &img_role3l);
            break;
        case 3:
            transparentimage(NULL, role_x, role_y, &img_role4l);
            break;
        case 4:
            transparentimage(NULL, role_x, role_y, &img_role5l);
            break;
        case 5:
            transparentimage(NULL, role_x, role_y, &img_role6l);
            break;
        case 6:
            transparentimage(NULL, role_x, role_y, &img_role7l);
            break;
        case 7:
            transparentimage(NULL, role_x, role_y, &img_role8l);
            break;
        case 8:
            transparentimage(NULL, role_x, role_y, &img_role9l);
            break;
        case 9:
            transparentimage(NULL, role_x, role_y, &img_role10l);
            break;
        default:
            break;
        }
    }
    else if (judge == 2)
    {
        switch (right)
        {
        case 0:
            transparentimage(NULL, role_x, role_y, &img_role1r);
            break;
        case 1:
            transparentimage(NULL, role_x, role_y, &img_role2r);
            break;
        case 2:
            transparentimage(NULL, role_x, role_y, &img_role3r);
            break;
        case 3:
            transparentimage(NULL, role_x, role_y, &img_role4r);
            break;
        case 4:
            transparentimage(NULL, role_x, role_y, &img_role5r);
            break;
        case 5:
            transparentimage(NULL, role_x, role_y, &img_role6r);
            break;
        case 6:
            transparentimage(NULL, role_x, role_y, &img_role7r);
            break;
        case 7:
            transparentimage(NULL, role_x, role_y, &img_role8r);
            break;
        case 8:
            transparentimage(NULL, role_x, role_y, &img_role9r);
            break;
        case 9:
            transparentimage(NULL, role_x, role_y, &img_role10r);
            break;
        default:
            break;
        }
    }
    FlushBatchDraw();
}

void show() //显示画面
{
    putimage(bk_x, bk_y, &img_bk);

    RoleWalk(step_left, step_right, moveDeriction);
    FlushBatchDraw();
}

void updateWithoutInput() //与输入无关的更新
{
    if (role_y > 555)
    {
        mciSendString("close bkmusic", NULL, 0, NULL);
        mciSendString("close swmusic", NULL, 0, NULL);
        mciSendString("open Music\\死亡.mp3 alias swmusic", NULL, 0, NULL);
        mciSendString("play swmusic", NULL, 0, NULL); //仅播放一次音乐
        Sleep(2500);
        system("pause");
        exit(0);
    }

    judgeOperate = 1; //确保每次循环都是从可行走开始

    if (judgeJump == 0 && role_y < flour) //没有跳高情况下
    {
        role_y += speed_y;
        real_y += speed_y;
    }
    if (judgeJump == 1)
    {
        role_y -= speed_y * 2;
        real_y -= speed_y * 2;
        jumpHigh += speed_y * 2;
        if (jumpHigh >= jumpHighTop)
        {
            judgeJump = 0;
            jumpHigh = 0;
        }
    }

    for (int i = 0; i < 3; i++) //坑地下落判断
    {
        if (real_x + roleWidth / 2 > KD[i].start_x && real_x + roleWidth / 2 < KD[i].end_x || real_y > flour)
        {
            if (judgeJump == 0)
            {
                role_y += speed_y;
                real_y += speed_y;
            }
        }
    }
    for (int i = 0; i < 6; i++) // 站在管道上的判断
    {
        if (real_x + roleWidth >= GD[i].start_x && real_x <= GD[i].end_x && real_y + roleHigh >= GD[i].zc_high + 10)
        {
            role_y -= speed_y;
            real_y -= speed_y;
        }
    }

    for (int i = 0; i < 26; i++) //站在不可破坏的砖块的判断
    {
        if (real_x + roleWidth >= BKPH[i].start_x && real_x <= BKPH[i].end_x && real_y + roleHigh >= BKPH[i].zc_high + 10)
        {
            role_y -= speed_y;
            real_y -= speed_y;
        }
    }

    if (moveDeriction == 1) //向左行走对阻挡的判断
    {
        for (int i = 0; i < 6; i++) //管道判断
        {
            if ((real_x >= GD[i].end_x + 1 && real_x <= GD[i].end_x + 5 && real_y + roleHigh >= GD[i].zc_high))
                judgeOperate = 0;
        }
    }

    if (moveDeriction == 2) //向右行走对阻挡的判断
    {
        for (int i = 0; i < 6; i++) //管道判断
        {
            if ((real_x + roleWidth >= GD[i].start_x - 5 && real_x + roleWidth <= GD[i].start_x && real_y + roleHigh >= GD[i].zc_high))
                judgeOperate = 0;
        }
    }
}

void updateWithInput() //与输入有关的更新
{

    if ((GetAsyncKeyState(0x44) & 0x8000)) //d
    {
        moveDeriction = 2;
        if (role_x >= Width / 2 && bk_x > Width - pictureWidth && judgeOperate == 1)
        {
            bk_x -= speed_x;
            real_x += speed_x;
            step_right++;
        }
        else if (role_x < pictureWidth && judgeOperate == 1)
        {
            role_x += speed_x;
            real_x += speed_x;
            step_right++;
        }
    }
    if ((GetAsyncKeyState(0x41) & 0x8000)) //a
    {
        moveDeriction = 1;
        if (role_x <= Width / 2 && bk_x > 0 && judgeOperate == 1)
        {
            bk_x += speed_x;
            real_x -= speed_x;
            step_left++;
        }
        else if (role_x > 0 && judgeOperate == 1)
        {
            role_x -= speed_x;
            real_x -= speed_x;
            step_left++;
        }
    }
    if ((GetAsyncKeyState(0x57) & 0x8000)) //跳跃
    {
        if (role_y >= flour)
            judgeJump = 1;
        if (real_y == 415)
        {
            mciSendString("close jpmusic", NULL, 0, NULL);
            mciSendString("open Music\\跳跃.mp3 alias jpmusic", NULL, 0, NULL);
            mciSendString("play jpmusic", NULL, 0, NULL); //仅播放一次音乐
        }
    }

    if (step_right >= 9)
        step_right = 0;
    if (step_left >= 9)
        step_left = 0;
}

int main(void)
{
    startup();
    while (1)
    {
        show();
        updateWithoutInput();
        updateWithInput();
        Sleep(10);
        cleardevice();
    }
    return 0;
}