from manim import *
import numpy as np
class a1(MovingCameraScene):
    def construct(self):
        dayere = Circle()
        
        
        self.play(self.camera.frame.animate.set(width=10),run_time=0.0001)
        
        self.wait(0.7)
        self.play(Write( dayere),run_time=3)
        self.wait(0.7)

class a2(MovingCameraScene):
    def construct(self):

        dayere = Circle()
        
        self.play(self.camera.frame.animate.set(width=10),run_time=0.0001)
        
        a=2
        '''axes = Axes(x_range=[-a,a,1], y_range=[-a,a,1],
        x_length = 2*a, y_length= 2*a)
        axes.add_coordinates()'''
        my_plane = NumberPlane(x_range=[-a,a,1], y_range=[-a,a,1],
        x_length = 2*a, y_length= 2*a) 
        #my_plane.add_coordinates()
        shoaa = Line(start=dayere.get_center() , end=dayere.get_right(), stroke_width=6)
        self.add( dayere )
        self.wait(0.3)
        self.play(Write(my_plane),run_time=1.5)
        self.wait(0.2)
        self.play(Create(shoaa),run_time=1.5)
        self.wait(5)
class a3(MovingCameraScene):
    def construct(self):
        dayere = Circle()
        
        self.play(self.camera.frame.animate.set(width=10),run_time=0.0001)
        
        a=2
        my_plane = NumberPlane(x_range=[-a,a,1], y_range=[-a,a,1],
        x_length = 2*a, y_length= 2*a) 
        
        #my_plane.add_coordinates()
        
        shoaa = Line(start=dayere.get_center() , end=dayere.get_right(), stroke_width=6)
        
        axes = Axes(x_range=[-a,a,1], y_range=[-a,a,1],
        x_length = 2*a, y_length= 2*a)
        axes.add_coordinates()
        
        axes_labels = axes.get_axis_labels(x_label="x",y_label="y")

        noghte = Dot(point=dayere.get_right(),color=RED).scale(2)
        
        self.add(shoaa, dayere ,my_plane)
        
        self.wait(0.5)
        self.play(Create(noghte),run_time=2)
        self.wait()
        self.play(Write(axes),Write(axes_labels),run_time=3)
        self.wait(5)
        

class a4(MovingCameraScene):
    def construct(self):
        dayere = Circle()
        
        self.play(self.camera.frame.animate.set(width=10),run_time=0.0001)
        
        a=2
        alpha= ValueTracker(0)
        my_plane = NumberPlane(x_range=[-a,a,1], y_range=[-a,a,1],
        x_length = 2*a, y_length= 2*a) 
        
        axes = Axes(x_range=[-a,a,1], y_range=[-a,a,1],
        x_length = 2*a, y_length= 2*a)
        axes.add_coordinates()
        
        axes_labels = axes.get_axis_labels(x_label="x",y_label="y")

        noghte = always_redraw(lambda:
        Dot(point=dayere.point_from_proportion(alpha.get_value())+np.array((0, 0.00001,0)) ,color=RED).scale(2))
        
        shoaa = Line(start=dayere.get_center() , end=dayere.get_right(), stroke_width=6)
        shoaa2 = always_redraw(lambda:
        Line(start=dayere.get_center() , end=dayere.point_from_proportion(alpha.get_value())+np.array((0, 0.00001,0)) , stroke_width=6)
        )
        hashiye = always_redraw(lambda:
        Angle(shoaa , shoaa2)
        )
        zaviye = VGroup(shoaa2 , hashiye)



        self.add(shoaa  , noghte  , axes_labels, dayere ,zaviye, my_plane, axes)
        
        self.play(alpha.animate.set_value(1),run_time=7,rate_func=rate_functions.linear)
        self.wait(4)
        

