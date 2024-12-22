import pygame
from pygame.math import Vector2
pygame.init()
pygame.mixer.init()
import sys, array


from .colors import *
from .managers import *
from . import scenes

class Window():
    def __init__(self, path: str, res: tuple, fpsLimit: int = 60):
        self.path = path
        self.res = Vector2(res)
        self.window = pygame.display.set_mode(self.res)#, pygame.OPENGL | pygame.DOUBLEBUF)
        self.screen = pygame.Surface(self.res)
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.bg = BLACK
        self.fpsLimit = fpsLimit

        #self.font = font
        self.music_volume = 0.1
        self.volume = 0.1

        #Defining the shader
        #self.ctx = moderngl.create_context()
        #self.quad_buffer = self.ctx.buffer(data = array.array('f', [
        #    #position  UV cord
        #    -1.0, 1.0, 0.0, 0.0,  # Top Left
        #    1.0, 1.0, 1.0, 0.0,   #Top Right
        #    -1.0, -1.0, 0.0, 1.0, #Bottom Left
        #    1.0, -1.0, 1.0, 1.0   #Bottom Right
        #    ]))
        #self.vertex_shader = ""
        #self.frag_shader = ""

        #with open(f"{self.path}\\shader\\vert.glsl", "r") as f:
        #    self.vertex_shader = f.read()
        #with open(f"{self.path}\\shader\\frag.glsl", "r") as f:
        #    self.frag_shader = f.read()

        #self.program = self.ctx.program(vertex_shader = self.vertex_shader, fragment_shader = self.frag_shader)
        #self.render_object = self.ctx.vertex_array(self.program, [(self.quad_buffer, "2f 2f", "vert", "texcoord")])

        self.scenes = []
        self.scene_manager = scenes.SceneManager(self, self.scenes)#, Transition)
        self.music_manager = None
        self.bloom = 3.0

        self.fullscreen = False

    #def surf_to_texture(self, surf):
    #                                      #color channels
    #    tex = self.ctx.texture(surf.get_size(), 4)
    #    tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
    #    tex.swizzle = "BGRA"
    #    tex.write(surf.get_view("1"))
    #    return tex

    def update(self):
        self.scene_manager.update_scene()
        if self.music_manager:
            self.music_manager.update()

    def draw(self):
        self.screen.fill(self.bg)
        self.scene_manager.draw_scene()
        self.window.blit(self.screen, self.screen.get_rect())

    def run(self):
        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_f:
                        if not self.fullscreen:
                            self.window = pygame.display.set_mode((self.res.x, self.res.y), pygame.OPENGL | pygame.DOUBLEBUF | pygame.FULLSCREEN)
                        else:
                            self.window = pygame.display.set_mode((self.res.x, self.res.y), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
                        self.fullscreen = not self.fullscreen
            self.draw()

            self.update()

            #frame_tex = self.surf_to_texture(self.screen)
            #frame_tex.use(0)

            #self.program["tex"] = 0
            #self.program["bg"] = self.bg
            #self.program["res"] = self.res
            #self.program["blurRadius"] = self.bloom
            #self.render_object.render(mode=moderngl.TRIANGLE_STRIP)

            pygame.display.flip()

            #frame_tex.release()

            self.clock.tick(self.fpsLimit)