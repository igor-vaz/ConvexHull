import OpenGL 
OpenGL.ERROR_ON_COPY = True 

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

global Points

def init2D(r,g,b):
	glClearColor(r,g,b,0.0)    
	glMatrixMode (GL_PROJECTION)
	gluOrtho2D (0.0, 500.0, 0.0, 500.0)

def display():
	global Points
	glClear(GL_COLOR_BUFFER_BIT)

	glPointSize(10)
	glColor3f(1.0, 1.0, 1.0)
	print Points
	if len(Points) > 0:
		#draw two points
		glBegin(GL_POINTS)
		for point in Points:
			glVertex2i(point[1],point[0])
		glEnd()

	glutSwapBuffers()
	#glFlush()


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
	global window
	# If escape is pressed, kill everything.
	if args[0] == ESCAPE:
		sys.exit()

def Upon_Click (button, button_state, cursor_x, cursor_y):
	""" Mouse button clicked.
		Glut calls this function when a mouse button is
		clicked or released.
	"""
	global Points
	# Mouse Scroll
	if button == 3:
		zoom += float(button_state)/4
	if button == 4:
		zoom -= float(button_state)/4

	if (button == GLUT_LEFT_BUTTON and button_state == GLUT_DOWN):	
		# Left button clicked down
		Points.append([cursor_x, cursor_y])

Points = []
glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (500, 500)
glutInitWindowPosition (100, 100)
glutCreateWindow ('points and lines')
# Register the function called when the keyboard is pressed.  
glutKeyboardFunc(keyPressed)
# GLUT When mouse buttons are clicked in window
glutMouseFunc (Upon_Click)
# 2D view
init2D(0.0,0.0,0.0)
glutDisplayFunc(display)
glutMainLoop()