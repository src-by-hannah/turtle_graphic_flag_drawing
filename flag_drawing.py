# Python 3.7
# -*- coding: utf-8 -*-
"""
Created on Thu April 4 11:28:16 2019

@author: src-by-hannah
Development of a Flag Production Program Using Turtle Library
"""

import turtle as t

'''
전역 변수 설정 
'''
a = 0
w, h = 0, 0 # 도형의 가로(width), 세로(height)
x_plus, y_plus = 0, 0 # x증가값, y증가값
x_turtle, y_turtle = 0, 0 # 거북이 현재 위치
r, g, b = 0, 0, 0 # red, green, blue
radius = 0 # 반지름
swidth, sheight = 0, 0 # screen 크기 설정

''' 
functions 
'''
# 직사각형 그리기 (가로, 세로, red, green, blue)
def rectangle(w, h, r, g, b) :
    t.color(r, g, b)
    t.begin_fill()
    t.pendown()
    
    for i in range(0, 2, 1) :
        t.forward(w)
        t.left(90)
        t.forward(h)
        t. left(90)

    t.end_fill()
    t.penup()
    
# 태극 반쪽 (반지름, red, green, blue)
def half_taegeug(radius, r, g, b) :
    t.color((r, g, b))
    t.begin_fill()
    t.pendown()
    t.circle(radius/2, -180)
    t.circle(radius, 180)
    t.circle(radius/2, 180)
    t.end_fill()
    t.penup()
    
 # 정별다각형 그리기 (푸앵소의 별)  (별의 중심 x좌표, 별의 중심 y좌표, 별의 꼭짓점 수, 인터벌, 원의 반지름(즉, 원점부터 꼭짓점 사이의 거리), red, green, blue)
def poinsot(x_star, y_star, n, k, radius, r, g, b) :
    t.color((r, g, b))
    rotation = int(360/n)

    list1, star_point = [], [] #star_point라는 리스트에 2차원 리스트 형태로 각 꼭짓점의 좌표가 저장된다.

    t.goto(x_star, y_star)
    t.setheading(90)
    
    # 원을 n등분 하는 원 위의 점의 좌표들을 리스트로 저장한다. (즉, 꼭짓점의 좌표)
    for i in range (0, n, 1) :
        t.setheading((90+rotation*i)) # 회전, +rotation인 이유 : 푸앵소의 별 공식 시계 반대방향으로 진행됨.
        t.forward(radius)
        
        list1.append(t.xcor()) # x좌표 추가
        list1.append(t.ycor()) # y좌표 추가
        star_point.append(list1) # star_point 리스트에 [x, y]좌표를 '리스트'형태로 추
        list1 = []

        t.goto(x_star, y_star) # 다시 원점으로

    t.goto(star_point[0][0], star_point[0][1])
    t.begin_fill()
    t.pendown()
    k1 = k
    for i in range (0, n, 1) :
        t.goto(star_point[k][0], star_point[k][1]) # k번째 꼭짓점으로 이동
        k = k + k1
        if k >= n :
               k = k-n # k값이 n을 넘는다면 k-n을 해준다.
    t.end_fill()
    t.penup()

# 달 그리기 
#(달의 한 꼭짓점 x 좌표, 달의 한 꼭짓점 y 좌표, 거북이의 초기 시작 각도, 바깥원 그리는 범위, 바깥원 반지름, 안쪽원-바깥원 사이 각도, 안쪽원 그리는 범위, 안쪽원 반지, r, g, b)
def moon(x_moon, y_moon, t_angle, outCircle_angle, outCircle_radius, betweenCircle_angle, inCircle_angle, inCircle_radius, r, g, b) :
    t.goto(x_moon, y_moon)
    t.color((r, g, b))
    t.setheading(t_angle)
    t.begin_fill()
    t.pendown()
    t.circle(outCircle_radius/2, outCircle_angle)
    t.right(betweenCircle_angle)
    t.circle(inCircle_radius/2, -inCircle_angle)
    t.end_fill()
    t.penup()
    
# 2:3비율의 국기 스크린 설정
def twothree() :
    swidth = 600; sheight = 400
    t.setup(width = swidth+15, height = sheight+15)
    t.screensize(swidth, sheight)
    
# 1:2비율의 국기 스크린 설정
def onetwo() :
    swidth = 600; sheight = 300
    t.setup(width = swidth+15, height = sheight+15)
    t.screensize(swidth, sheight)
    
''' 
class, method 
'''
class draw_flag :
    #대한민국 국기 그리기 (2: 3)
    def korea(self) :
        t.penup()
        twothree()
        # 태극문양 그리기 : half_taegeug(radius, r, g, b)
        ## 빨간색 부분
        t.left(270)
        half_taegeug(100, 205, 49, 58)

        ## 파란색 부분
        half_taegeug(100, 0, 71,160)


        # 사괘 그리기 : rectangle(w, h, r, g, b)
        ## 건
        for i in range (0, 3, 1) :
            x_plus, y_plus = (-21)*i, 14*i
            t.goto(-164+x_plus, 51+y_plus)
            t.setheading(326)
            rectangle(17, 100, 14, 14, 14)

        ## 리
        ### 작은 직사각형
        for i in range (0, 2, 1) :
            x_plus, y_plus = 30*i, (-45)*i
            t.goto(-164-21+x_plus, -51-14+y_plus)
            t.setheading(304)
            rectangle(46, 17, 14, 14, 14)

        ### 큰 직사각형
        for i in range(0, 3, 2) :
            x_plus, y_plus = (-21)*i, (-14)*i
            t.goto(-164+x_plus, -51+y_plus)
            t.setheading(304)
            rectangle(100, 17, 14, 14, 14)

        ## 곤
        for i in range (0, 3, 1) :
            x_plus, y_plus = 21*i, (-14)*i
            t.goto(164+x_plus, -51+y_plus)
            x_turtle = t.xcor()
            y_turtle = t.ycor()
    
            for j in range(0, 2, 1) :
                x_plus, y_plus = (-30)*j, (-45)*j
                t.goto(x_turtle+x_plus, y_turtle+y_plus)
                t.pendown()
                t.setheading(146)
                rectangle(17, 46, 14, 14, 14)
                t.penup()

        ## 감
        ### 작은 직사각형
        for i in range (0, 3, 2) :
            x_plus, y_plus = 21*i, 14*i
            t.goto(164+x_plus, 51+y_plus)
            x_turtle = t.xcor()
            y_turtle = t.ycor()
    
            for j in range(0, 2, 1) :
                x_plus, y_plus = (-30)*j, 45*j
                t.goto(x_turtle+x_plus, y_turtle+y_plus)
                t.pendown()
                t.setheading(124)
                rectangle(46, 17, 14, 14, 14)
                t.penup()

        ### 큰 직사각형
        t.goto(164+21, 51+14)
        t.pendown()
        t.setheading(124)
        rectangle(100, 17, 14, 14, 14)
        t.penup()

        t.hideturtle()
    
    # 네덜란드 국기 그리기 (2:3)
    def netherlands(self) :
        t.penup()
        twothree()
        #빨간 직사각형 그리기 : rectangle(w, h, r, g, b)
        t.goto(-300, 67) #(-(600/2) , +(400/2-400/3))
        rectangle(600, 133, 174, 28, 40)

        #파란 직사각형 그리기 : rectangle(w, h, r, g, b)
        t.goto(-300, -200)
        rectangle(600, 133, 33, 70, 139)
        
        t.hideturtle()
        
    # 프랑스 국기 그리기 (2:3)
    def france(self) :
        t.penup()
        twothree()
        #파란 직사각형 그리기 : rectangle(w, h, r, g, b)
        t.goto(-300, -200)
        rectangle(200, 400, 0, 85, 164)

        #빨간 직사각형 그리기 : rectangle(w, h, r, g, b)
        t.goto(100, -200)
        rectangle(200, 400, 239, 65, 53)
        
        t.hideturtle()
        
    # 인도 국기 그리기 (2:3)
    def india(self) :
        t.penup()
        twothree()
        # 주황색 직사각형 그리기 : rectangle(w, h, r, g, b)
        t.goto(-300, 67) #(-300, (200-133))
        rectangle(600, 133, 255, 153, 51)

        # 초록색 직사각형 그리기 : rectangle(w, h, r, g, b)
        t.goto(-300, -200)
        rectangle(600, 133, 18, 136, 7)

        # 원 그리기
        ## 파란색 바깥 원 그리기
        t.goto(54, 0)
        t.setheading(90)
        t.color((0, 0, 136))
        t.begin_fill()
        t.pendown()
        t.circle(54)
        t.end_fill()
        t.penup()

        ## 흰색 안쪽 원 그리기
        t.goto(47, 0)
        t.setheading(90)
        t.color((255, 255, 255))
        t.begin_fill()
        t.pendown()
        t.circle(47)
        t.end_fill()
        t.penup()


        ## 가운데 파란색 원 그리기
        t.goto(9, 0)
        t.setheading(90)
        t.color((0, 0, 136))
        t.begin_fill()
        t.pendown()
        t.circle(9)
        t.end_fill()
        t.penup()

        # 문양 그리기
        n = 24 # n : 문양의 개수
        rotation = 360/n
        for i in range (0, 24, 1) :
            # 검 문양 그리기
    
            t.goto(0,0)
            t.setheading(int(90 + rotation*i))

            t.begin_fill()
            t.pendown()
    
            t.forward(47)
            t.setheading(int(266.32 + rotation*i))
            t.forward(28.06)
            t.setheading(int(275.4 + rotation*i))
            t.forward(19.09)
            t.setheading(int(84.59 + rotation*i))
            t.forward(19.09)
            t.setheading(int(93.68 + rotation*i))
            t.forward(28.06)

            t.end_fill()
            t.penup()

            # 작은 원 그리기
            t.goto(0,0)
            t.setheading(int(90 + rotation*(i-1) + (rotation)/2))
            t.forward(47)
            t.color((0, 0, 136))
            t.begin_fill()
            t.pendown()
            
            t.circle(2.3)
            
            t.end_fill()
            t.penup()

        t.hideturtle()
        
    # 캐나다 국기 그리기 (1:2)
    def canada(self) :
        t.penup()
        onetwo()
        # 양 사이드 빨간 직사각형 그리기
        t.goto(-300, -150)
        rectangle(150, 300, 255, 0, 0)
        t.goto(150, -150)
        rectangle(150, 300, 255, 0, 0)

        # 나뭇잎 그리기
        maple = [[0, 125], [-23, 82], [-47, 94], [-36, 25], [-68, 53], [-76, 36], [-112, 43], [-101, 5], [-116, -4], [-56, -53], [-64, -76], [-5, -68], [-6, -125], [0, -125]]
        
        t.goto(maple[0][0], maple[0][1])
        t.color((255, 0, 0))
        t.begin_fill()
        t.pendown()
        for i in range (1, 14, 1) :
            t.goto((maple[i][0]), (maple[i][1]))
        for i in range (0, 14, 1) :
            t.goto(-(maple[(13-i)][0]), maple[(13-i)][1]) # 역으로 출력(데칼코마니)
        t.end_fill()
        t.penup()

        t.hideturtle()
        
    # 말레이시아 국기 그리기 (1:2)
    def malaysia(self) :
        t.penup()
        onetwo()
        # 빨간색 직사각형 그리기 : (w, h, r, g, b)
        for i in range(0, 14, 2) :
            t.goto(-300, (129-21*i))
            rectangle(600, 21, 220, 36, 31)

        # 파란색 직사각형 그리기 : (w, h, r, g, b)
        t.goto(-300, -18)
        rectangle(300, 168, 0, 53, 173)

        # 별 그리기 : (x_star, y_star, n, k, radius, r, g, b)
        poinsot(-110, 65, 14, 5, 50, 255, 209, 0)

        # 달 그리기 : (x_moon, y_moon, t_angle, outCircle_angle, outCircle_radius, betweenCircle_angle, inCircle_angle, inCircle_radius, r, g, b)
        moon(-160, 110, 134.94, 269.92, 125, 16.49, 237.04, 100, 255, 209, 0)

        t.hideturtle()
        
    # 영국 국기 그리기 (1:2)
    def uk(self) :
        t.penup()
        onetwo()
        # 배경 색 blue로 변경
        t.bgcolor((0, 36, 125))

        # 흰색 X자 부분 그리기 : (w, h, r, g, b)
        t.goto(-300, 150)
        t.setheading(333)
        rectangle(671, 30, 255, 255, 255)
        
        t.setheading(333-90)
        rectangle(30, 671, 255, 255, 255)
        
        t.goto(300, 150)
        t.setheading(360-333+180)
        rectangle(671, 30, 255, 255, 255)
        
        t.setheading(360-333+180-90)
        rectangle(30, 671, 255, 255, 255)
        
        # 빨간색 X자 부분 그리기 : (w, h, r, g, b)
        t.goto(-300, 150)
        t.setheading(333-90)
        rectangle(20, 336, 207, 20, 43)
        
        t.goto(0, 0)
        t.setheading(333)
        rectangle(336, 20, 207, 20, 43)
        
        t.goto(0, 0)
        t.setheading(360-333+180)
        rectangle(336, 20, 207, 20, 43)
        
        t.goto(300, 150)
        t.setheading(360-333+180-90)
        rectangle(20, 336, 207, 20, 43)
        
        # 흰색 + 부분 그리기 : (w, h, r, g, b)
        t.goto(-300, -50)
        t.setheading(0)
        rectangle(600, 100, 255, 255, 255)
        
        t.goto(-50, -150)
        t.setheading(0)
        rectangle(100, 600, 255, 255, 255)
        
        # 빨간색 + 부분 그리기
        t.goto(-300, -30)
        t.setheading(0)
        rectangle(600, 60, 207, 20, 43)
        
        t.goto(-30, -150)
        t.setheading(0)
        rectangle(60, 600, 207, 20, 43)
        
        t.hideturtle()

    # 네팔 국기 그리기 (5:4)
    def nepal(self) :
        t.penup()
        # 스크린 설정
        swidth = 400; sheight = 500
        t.setup(width = swidth+30, height = sheight+30)
        t.screensize(swidth, sheight)
        
        # 파랑색 겉 테두리 그리기
        t.color((0, 56, 147))
        t.begin_fill()

        t.goto(-200, 250)
        t.pendown()
        t.goto(200, -15)
        t.goto(-55, -15)
        t.goto(185, -250)
        t.goto(-200, -250)
        t.goto(-200, 250)
        t.end_fill()
        t.penup()

        # 빨강색 속 그리기
        t.color((220, 20, 60))
        t.begin_fill()
                   
        t.goto(-185, 220)
        t.pendown()
        t.goto(150, 2)
        t.goto(-90, 2)
        t.goto(150, -235)
        t.goto(-185, -235)
        t.goto(-185, 220)
        t.end_fill()
        t.penup()

        # 하단 별 문양 그리기 : (x_star, y_star, n, k, radius, r, g, b)
        poinsot(-100, -120, 12, 5, 60, 255, 255, 255) #(n=12, k=5)

        # 상단 달 + 별 문양 그리기 
        # poinsot(x_star, y_star, n, k, radius, r, g, b)
        # moon(x_moon, y_moon, t_angle, outCircle_angle, outCircle_radius, betweenCircle_angle, inCircle_angle, inCircle_radius, r, g, b)
        poinsot(-100, 55, 16, 5, 40, 255, 255, 255)
        moon(-170, 80, 270, 180, 140, 30.56, 118.98, 162.5, 255, 255, 255)
        
        t.hideturtle()
        
    # 미국 국기 그리기 (10:19)
    def usa(self) :
        t.penup()
        # screen 설정
        swidth, sheight = 570, 300
        t.setup(width = swidth + 30, height = sheight + 30)
        t.screensize(swidth, sheight)
        
        # 빨간색 직사각형 그리기 : (w, h, r, g, b)
        for i in range(0, 14, 2) :
            t.goto(-285, (127-23*i))
            rectangle(570, 23, 177, 35, 50)
            
        # 파란색 직사각형 그리기 : (w, h, r, g, b)
        t.goto(-285, -12)
        rectangle(228, 162, 0, 38, 100)
        
        # 별 채우기 : (x_star, y_star, n, k, radius, r, g, b)
        ## 한 줄에 6개
        for i in range (0, 5, 1) :
            if i == 0:
                t.goto(-266, 132)
            else :
                t.goto((x_turtle-190), (y_turtle-32)) # 하단으로 이동
            # 한 줄에 별 6개 그리기
            for j in range(0, 6, 1) :
                x_turtle = t.xcor()
                y_turtle = t.ycor()
                poinsot(x_turtle, y_turtle, 5, 2, 9, 255, 255, 255)
                t.goto((x_turtle+38), y_turtle)
        ## 한 줄에 5개
        for i in range (0, 4, 1) :
            if i == 0:
                t.goto(-247, 118)
            else :
                t.goto((x_turtle-152), (y_turtle-32)) # 하단으로 이동
            # 한 줄에 별 5개 그리기
            for j in range(0, 5, 1) :
                x_turtle = t.xcor()
                y_turtle = t.ycor()
                poinsot(x_turtle, y_turtle, 5, 2, 9, 255, 255, 255)
                t.goto((x_turtle+38), y_turtle)
            
        t.hideturtle()
    
''' 
main 
'''
if __name__ == "__main__" :
    while True :
        a = int(input("""Turtle이 그릴 국기를 선택하시오.
(국기 사이 실행 시간 간격 : 5초)

1. 대한민국(Korea)
2. 네덜란드(Netherlands)
3. 프랑스(France)
4. 인도(India)
5. 캐나다(Canada)
6. 말레이시아(Malaysia)
7. 영국(UK)
8. 네팔(Nepal)
9. 미국(USA)
10. 전체 PLAY
0. 종료
                      
선택 >>> """))
        
        #turtle 기본 설정
        t.title('Turtle Graphic을 이용한 만국기 그리기')
        t.shape('circle')
        t.colormode(255)
        t.speed('fastest')
        
        df = draw_flag()
        
        if a==1 :
            t.ontimer(df.korea(), 5000)
            t.reset()
        
        elif a==2 :
            t.ontimer(df.netherlands(), 5000)
            t.reset()
            
        elif a==3 :
            t.ontimer(df.france(), 5000)
            t.reset()
            
        elif a==4 :
            t.ontimer(df.india(), 5000)
            t.reset()
            
        elif a==5 :
            t.ontimer(df.canada(), 5000)
            t.reset()
            
        elif a==6 :
            t.ontimer(df.malaysia(), 5000)
            t.reset()
        
        elif a==7 :
            t.ontimer(df.uk(), 5000)
            t.reset()
            t.bgcolor((255, 255, 255))
            
        elif a==8 :
            t.ontimer(df.nepal(), 5000)
            t.reset()
            
        elif a==9 :
            t.ontimer(df.usa(), 5000)
            t.reset()
        
        elif a==10 :
            t.ontimer(df.korea(), 5000)
            t.reset()
            t.speed('fastest')
            t.ontimer(df.netherlands(), 5000)
            t.reset()
            t.speed('fastest')
            t.ontimer(df.france(), 5000)
            t.reset()
            t.speed('fastest')
            t.ontimer(df.india(), 5000)
            t.reset()
            t.speed('fastest')
            t.ontimer(df.canada(), 5000)
            t.reset()
            t.speed('fastest')
            t.ontimer(df.malaysia(), 5000)
            t.reset()
            t.speed('fastest')
            t.ontimer(df.uk(), 5000)
            t.reset()
            t.bgcolor((255, 255, 255))
            t.speed('fastest')
            t.ontimer(df.nepal(), 5000)
            t.reset()
            t.speed('fastest')
            t.ontimer(df.usa(), 5000)
            t.reset()

        elif a==0 :
            print("종료합니다.")
            t.done()
            break
        
        else :
            print("1~10 사이의 숫자 중에서 다시 고르시오.")
            print()
