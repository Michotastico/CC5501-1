__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from tools.algorithm.QuickHull import QuickHull
from tools.algorithm import RandomFactory

import Bottle
import Can
import SpriteBottle
import TwoFigures



#cloud = SpriteBottle.point_cloud
cloud = TwoFigures.figures()
cloud2 = TwoFigures.figures()
'''
cloud = list()
RandomFactory.make_points(0, 10, 100)
for p in points_list:
    cloud.append(p)'''


qhull = QuickHull(cloud, 0)
qhull.run()
faces = qhull.get_faces()

for e in faces:
    if e.a() in cloud2:
        cloud2.remove(e.a())
    if e.b() in cloud2:
        cloud2.remove(e.b())
    if e.c() in cloud2:
        cloud2.remove(e.c())

qhull2 = QuickHull(cloud2, 0)
qhull2.run()
faces_2 = qhull2.get_faces()


# Values for Bottle: 0.09; Can: 0

#quick_hull = QuickHull(cloud, 0)
#quick_hull.run()
#faces = quick_hull.get_faces()


def figure():
    a = 0.0
    b = 0.1
    c = 0.2
    for f in faces:
        glBegin(OpenGL.GL.GL_TRIANGLES)
        glColor3f(a, b, c)
        glVertex3fv(f.a())
        glVertex3fv(f.b())
        glVertex3fv(f.c())
        glEnd()
        a += 0.001
        b += 0.001
        c += 0.001
    for f in faces_2:
        glBegin(OpenGL.GL.GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3fv(f.a())
        glVertex3fv(f.b())
        glVertex3fv(f.c())
        glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0, 0, -10)

    glRotatef(25, 2, 1, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_d:
                    glTranslatef(0.5, 0, 0)

                if event.key == pygame.K_w:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_s:
                    glTranslatef(0, -1, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)

                if event.button == 5:
                    glTranslatef(0, 0, -1.0)

        glRotatef(1, 3, 1, 1)
        glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT | OpenGL.GL.GL_DEPTH_BUFFER_BIT)
        figure()
        pygame.display.flip()
        pygame.time.wait(10)


main()
