import pygame
import pygame_gui


class DrawUIComponents:
    def __init__(self,manager,incoming_jobs,accepted_jobs,debug=False):
        self.manager = manager
        self.debug = debug
        self.incoming_jobs_str= []
        self.accepted_jobs_str= []
        for job in incoming_jobs:
            self.incoming_jobs_str.append("Job #" +str(job.number))
        for job in accepted_jobs:
            self.accepted_jobs_str.append("Job #" +str(job.number))
    def draw(self,current_time):
        manager =self.manager
        btn_next_day_rect = pygame.Rect(0, 0, 140, 30)
        btn_next_day_rect.topright = (-170, 50)
        self.btn_next_day = pygame_gui.elements.UIButton(relative_rect=btn_next_day_rect,
                                                     text='Next Day',
                                                     manager=manager,
                                                     anchors={'right':'right', 
                                                              'top':'top'},)
        btn_fast_forward_rect = pygame.Rect(0, 0, 140, 30)
        btn_fast_forward_rect.topright = (-10, 50)
        self.btn_fast_forward = pygame_gui.elements.UIButton(relative_rect=btn_fast_forward_rect,
                                                     text='Next Season',
                                                     manager=manager,
                                                     anchors={'right':'right', 
                                                              'top':'top'},)
        lbl_inc_jobs_rect = pygame.Rect(0, 0, 140, 30)
        lbl_inc_jobs_rect.topright = (-170, 90)
        self.lbl_inc_jobs = pygame_gui.elements.UILabel(relative_rect=lbl_inc_jobs_rect,
                                                        text='Incoming Jobs',
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)

        lst_inc_jobs_rect = pygame.Rect(0, 0, 300, 150)
        lst_inc_jobs_rect.topright = (-10, 120)
        self.lst_inc_jobs = pygame_gui.elements.UISelectionList(relative_rect=lst_inc_jobs_rect,
                                                     item_list=self.incoming_jobs_str,
                                                     manager=manager,
                                                     anchors={'right':'right',
                                                                    'top':'top'},)
        #Detail job
        lbl_det_job_rect = pygame.Rect(0, 0, 140, 30)
        lbl_det_job_rect.topright = (-170, 280)
        self.lbl_det_job = pygame_gui.elements.UILabel(relative_rect=lbl_det_job_rect,
                                                        text='Details Job',
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        lbl_det_num_rect = pygame.Rect(0, 0, 50, 30)
        lbl_det_num_rect.topright = (-260, 310)
        self.lbl_det_num = pygame_gui.elements.UILabel(relative_rect=lbl_det_num_rect,
                                                        text='No.',
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        txt_det_num_rect = pygame.Rect(0, 0, 100, 30)
        txt_det_num_rect.topright = (-160, 310)
        self.txt_det_num = pygame_gui.elements.UITextEntryLine(relative_rect=txt_det_num_rect,
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        lbl_det_num_tree_rect = pygame.Rect(0, 0, 50, 30)
        lbl_det_num_tree_rect.topright = (-260, 340)
        self.lbl_det_num_tree = pygame_gui.elements.UILabel(relative_rect=lbl_det_num_tree_rect,
                                                        text='# Tree',
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        txt_det_num_tree_rect = pygame.Rect(0, 0, 100, 30)
        txt_det_num_tree_rect.topright = (-160, 340)
        self.txt_det_num_tree = pygame_gui.elements.UITextEntryLine(relative_rect=txt_det_num_tree_rect,
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        lbl_det_area_rect = pygame.Rect(0, 0, 50, 30)
        lbl_det_area_rect.topright = (-100, 340)
        self.lbl_det_area = pygame_gui.elements.UILabel(relative_rect=lbl_det_area_rect,
                                                        text='Area',
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        txt_det_area_rect = pygame.Rect(0, 0, 100, 30)
        txt_det_area_rect.topright = (-10, 340)
        self.txt_det_area = pygame_gui.elements.UITextEntryLine(relative_rect=txt_det_area_rect,
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        lbl_det_tree_sit_rect = pygame.Rect(0, 0, 120, 30)
        lbl_det_tree_sit_rect.topright = (-190, 370)
        self.lbl_det_tree_sit = pygame_gui.elements.UILabel(relative_rect=lbl_det_tree_sit_rect,
                                                        text='Trees Situation',
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        txt_det_tree_sit_rect = pygame.Rect(0, 0, 170, 30)
        txt_det_tree_sit_rect.topright = (-10, 370)
        self.txt_det_tree_sit = pygame_gui.elements.UITextEntryLine(relative_rect=txt_det_tree_sit_rect,
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        lbl_det_gra_sit_rect = pygame.Rect(0, 0, 120, 30)
        lbl_det_gra_sit_rect.topright = (-190, 400)
        self.lbl_det_gra_sit = pygame_gui.elements.UILabel(relative_rect=lbl_det_gra_sit_rect,
                                                        text='Grass Situation',
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        txt_det_gra_sit_rect = pygame.Rect(0, 0, 170, 30)
        txt_det_gra_sit_rect.topright = (-10, 400)
        self.txt_det_gra_sit = pygame_gui.elements.UITextEntryLine(relative_rect=txt_det_gra_sit_rect,
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        txt_job_todo_rect = pygame.Rect(0, 0, 300, 30)
        txt_job_todo_rect.topright = (-10, 430)
        self.txt_job_todo = pygame_gui.elements.UITextEntryLine(relative_rect=txt_job_todo_rect,
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)

        txt_det_est_rect = pygame.Rect(0, 0, 100, 30)
        txt_det_est_rect.topright = (-210, 460)
        self.txt_det_est = pygame_gui.elements.UITextEntryLine(relative_rect=txt_det_est_rect,
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)

        lbl_det_est_rect = pygame.Rect(0, 0, 120, 30)
        lbl_det_est_rect.topright = (-90, 460)
        self.lbl_det_est = pygame_gui.elements.UILabel(relative_rect=lbl_det_est_rect,
                                                        text='Per Tree',
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)

        btn_det_est_rect = pygame.Rect(0, 0, 100, 30)
        btn_det_est_rect.topright = (-10, 460)
        self.btn_det_est = pygame_gui.elements.UIButton(relative_rect=btn_det_est_rect,
                                                     text='Estimate',
                                                     manager=manager,
                                                     anchors={'right':'right', 
                                                              'top':'top'},)


        lbl_acc_jobs_rect = pygame.Rect(0, 0, 140, 30)
        lbl_acc_jobs_rect.topright = (-170, 490)
        self.lbl_acc_jobs = pygame_gui.elements.UILabel(relative_rect=lbl_acc_jobs_rect,
                                                        text='Accepted Jobs',
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)

        lst_acc_jobs_rect = pygame.Rect(0, 0, 300, 120)
        lst_acc_jobs_rect.topright = (-10, 520)
        self.lst_acc_jobs = pygame_gui.elements.UISelectionList(relative_rect=lst_acc_jobs_rect,
                                                     item_list=self.accepted_jobs_str,
                                                     manager=manager,
                                                     anchors={'right':'right',
                                                                    'top':'top'},)
        lbl_hire_rect = pygame.Rect(0, 0, 120, 30)
        lbl_hire_rect.topright = (-190, 650)
        self.lbl_hire = pygame_gui.elements.UILabel(relative_rect=lbl_hire_rect,
                                                        text='--',
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        txt_hire_rect = pygame.Rect(0, 0, 100, 30)
        txt_hire_rect.topright = (-110, 650)
        self.txt_hire = pygame_gui.elements.UITextEntryLine(relative_rect=txt_hire_rect,
                                                        manager=manager,
                                                        anchors={'right':'right',
                                                                    'top':'top'},)
        btn_hire_rect = pygame.Rect(0, 0, 100, 30)
        btn_hire_rect.topright = (-10, 650)
        self.btn_hire = pygame_gui.elements.UIButton(relative_rect=btn_hire_rect,
                                                     text='Hire',
                                                     manager=manager,
                                                     anchors={'right':'right', 
                                                              'top':'top'},)
        btn_go_rect = pygame.Rect(0, 0, 300, 30)
        btn_go_rect.topright = (-10, 680)
        self.btn_go = pygame_gui.elements.UIButton(relative_rect=btn_go_rect,
                                                     text='Go to work!',
                                                     manager=manager,
                                                     anchors={'right':'right', 
                                                              'top':'top'},)

        date_text_rect = pygame.Rect(0, 0, 80, 30)
        date_text_rect.topright = (-230, 10)
        self.date_text = pygame_gui.elements.UITextBox(html_text= "63 $",
                                                     relative_rect=date_text_rect,
                                                     manager=manager,
                                                     anchors={'right':'right', 
                                                              'top':'top'},
                                                              )
        date_text_rect = pygame.Rect(0, 0, 200, 30)
        date_text_rect.topright = (-10, 10)
        self.date_text = pygame_gui.elements.UITextBox(html_text= current_time,
                                                     relative_rect=date_text_rect,
                                                     manager=manager,
                                                     anchors={'right':'right', 
                                                              'top':'top'},
                                                              )
        if self.debug:
            btn_gen_job_rect = pygame.Rect(0, 0, 300, 30)
            btn_gen_job_rect.topright = (-10, 710)
            self.btn_gen_job = pygame_gui.elements.UIButton(relative_rect=btn_gen_job_rect,
                                                         text='GenJob!',
                                                         manager=manager,
                                                         anchors={'right':'right', 
                                                                  'top':'top'},)
            
    def add_incoming_job(self,number):
        #self.incoming_jobs_str.append("Job #" +str(number))
        self.lst_inc_jobs.add_items(["Job #" +str(number)])
        #self.lst_inc_jobs.add_items(self.incoming_jobs_str)
    def remove_incoming_job(self,number):
        self.lst_inc_jobs.remove_items(["Job #" +str(number)])
        self.remove_detail()
    def add_accepted_job(self,job):
        #self.incoming_jobs_str.append("Job #" +str(number))
        self.lst_acc_jobs.add_items(["Job #" + f"{job.number:03}" + " - " + str(job.price) + "$ x tree - " + ", ".join(job.todo_list)])
        #self.lst_inc_jobs.add_items(self.incoming_jobs_str)
    def remove_detail(self):
        self.txt_det_num.set_text('')
        self.txt_det_num_tree.set_text('')
        self.txt_det_area.set_text('')
        self.txt_det_tree_sit.set_text('')
        self.txt_det_gra_sit.set_text('')
        self.txt_job_todo.set_text('')
    def show_detail(self,job):
        self.txt_det_num.set_text(str(job.number))
        self.txt_det_num_tree.set_text(str(int(job.n_olive_tree)))
        self.txt_det_area.set_text(str(job.width) +'x'+ str(job.height))
        self.txt_det_tree_sit.set_text(job.get_tree_situation())
        self.txt_det_gra_sit.set_text(job.get_grass_situation())
        self.txt_job_todo.set_text(", ".join(job.todo_list))
        #self.txt_det_job_type.set_text(job.job_type)
        #self.txt_det_job_size.set_text(str(job.job_size))
        #self.txt_det_gra_sit.set_text(job.grass_situation)
        #self.txt_det_est.set_text(str(job.estimate))