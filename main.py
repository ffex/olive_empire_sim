import pygame
from models import *
from draw_game import *
from game_time import GameTime
from ui_comp import DrawUIComponents
import pygame_gui

pygame.init()
pygame.mixer.init()
trimmer_sound = pygame.mixer.Sound("sounds/trimmer.wav")

pygame.display.set_caption('Olive Empire Sim')
game_screen_size= (1024, 768)
window_surface = pygame.display.set_mode(game_screen_size)
background = pygame.Surface(game_screen_size)
background.fill(pygame.Color('#000000'))
SECONDTICK = pygame.USEREVENT + 1000
pygame.time.set_timer(SECONDTICK, 1000)
is_running = True
play_game=False
current_job =None


draw_game = DrawGame(window_surface)

clock = pygame.time.Clock()
game_time=GameTime()

incoming_jobs =[Job(1, JobClass.E, game_time.current_tree_time)]
waiting_jobs =[]
accepted_jobs =[]
current_job_numb = 2
player = Player("ffex",(0,0),draw_game)
playerdir='s'
items = [Item("trimmer", pygame.image.load('images/dece.png'), (0, 0),True),
            Item("net", pygame.image.load('images/rete.png'), (1, 0),True,True,False),
            Item("prune_tools", pygame.image.load('images/pota.png'), (2, 0),True),
            Item("harvester", pygame.image.load('images/scuo.png'), (3, 0),True)
         ]


manager = pygame_gui.UIManager(game_screen_size,"textbox.json")
ui_component = DrawUIComponents(manager,incoming_jobs ,accepted_jobs,False)
ui_component.draw(game_time.get_current_time())

new_job = random.randint(0, 50)

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == SECONDTICK: 
            ui_component.date_text.set_text(game_time.update())
            new_job -=1
            if new_job<=0:
                incoming_jobs.append(Job(current_job_numb, JobClass.E,game_time.current_tree_time))
                ui_component.add_incoming_job(current_job_numb)
                current_job_numb += 1
                new_job = random.randint(0, 20)
            for job in waiting_jobs:
                if job.to_accept:
                    if job.accept_at <= game_time.seconds:
                        perc=random.randint(0, 100)
                        if perc >=50:
                            job.accepted=True
                            waiting_jobs.remove(job)
                            accepted_jobs.append(job)
                            #TODO, mettere la possibilita che non sia scelto
                            ui_component.add_accepted_job(job)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == ui_component.btn_next_day:
                ui_component.date_text.set_text(game_time.next_day())
            if event.ui_element == ui_component.btn_fast_forward:
                ui_component.date_text.set_text(game_time.fast_forward())
            if event.ui_element == ui_component.btn_det_est:
                for job in incoming_jobs:
                    if str(job.number) == ui_component.txt_det_num.text:
                        job.set_price(float(ui_component.txt_det_est.text),game_time.seconds)
                        waiting_jobs.append(job)
                        incoming_jobs.remove(job)
                        ui_component.remove_incoming_job(job.number)

            #if event.ui_element == ui_component.btn_gen_job:
            #    incoming_jobs.append(Job(current_job_numb, JobClass.E,game_time.current_tree_time))
            #    ui_component.add_incoming_job(current_job_numb)
            #    current_job_numb += 1
            if event.ui_element == ui_component.btn_go:
                if current_job != None:
                    play_game=True
                    draw_game.draw_map(current_job.matrix,player.position,items)
                    draw_game.draw_player(playerdir)
                    player.set_matrix(current_job.matrix)
                    #job.print_matrix()
                

        if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
            if event.ui_element == ui_component.lst_inc_jobs:
                for job in incoming_jobs:
                    if str(job.number) == event.text[5:]:
                        selected_job = job
                
                ui_component.show_detail(selected_job)
            if event.ui_element == ui_component.lst_acc_jobs:
                #print(event.text[5:8])
                for job in accepted_jobs:
                    if f"{job.number:03}" == event.text[5:8]:
                        current_job = job
        if play_game:
            no_move = True
            if event.type == pygame.KEYDOWN:
            
                #redrawmap(playermatrixpos[0],playermatrixpos[1],playerpos)

                if event.key == pygame.K_w:
                    #if positionallowed(playermatrixpos[0],playermatrixpos[1]-1):
                    #    playermatrixpos = playermatrixpos[0],playermatrixpos[1]-1
                    playerdir='n'
                    no_move=False
                if event.key == pygame.K_s:
                    #if positionallowed(playermatrixpos[0],playermatrixpos[1]+1):
                    #    playermatrixpos = playermatrixpos[0],playermatrixpos[1]+1
                    playerdir='s'
                    no_move=False
                if event.key == pygame.K_a:
                    #if positionallowed(playermatrixpos[0]-1,playermatrixpos[1]):
                    #    playermatrixpos = playermatrixpos[0]-1,playermatrixpos[1]
                    playerdir='o'
                    no_move=False
                if event.key == pygame.K_d:
                    #if positionallowed(playermatrixpos[0]+1,playermatrixpos[1]):
                    #    playermatrixpos = playermatrixpos[0]+1,playermatrixpos[1]
                    playerdir='e'
                    no_move=False
                if event.key == pygame.K_SPACE:
                    player.pickup(draw_game,items)
                if event.key == pygame.K_b:
                    player.drop()
                if event.key == pygame.K_v:
                    interacted = player.interact_on_ground(current_job.matrix[player.position[0]][player.position[1]],trimmer_sound)
                    if not interacted:
                        player.interact_on_direction(current_job.matrix,playerdir)
                    completed = current_job.check_if_completed()
                    if completed:
                        pass #TODO, aggiungere il pagamento
                    #draw_game.draw_map(current_job.matrix,player.position,items)
                    #draw_game.draw_player(playerdir)                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                        pass
                if no_move == False:
                    player.move(playerdir)
                draw_game.draw_map(current_job.matrix,player.position,items)
                draw_game.draw_player(playerdir)
                
                #redrawmap2(player.position)
                #redrawplayer(playerdir)
        manager.process_events(event)
    
    manager.update(time_delta)
    #window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()

