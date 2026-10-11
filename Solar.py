import customtkinter as ctk
from PIL import Image
import serial

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        #self.arduino=serial.Serial("COM3",9600,timeout=1)

        self.title("Solar")
        self.attributes("-fullscreen",True)

        self.usuario_login="Vinicius"
        self.usuario_senha="230610"


        self.construir_login()
        #self.tela_principal()
        #self.Criar_Conta()
        #self.barra_lateral()
        #self.dashboard()
        #self.diagnosticos()
        #self.relatorios()
        #self.configuracoes()

        #Acima declaração do front-end
        #Abaixo declaracao do back-end

        #self.verificar_login()
        #self.troca_tela()
        #self.ativar_automatico(
        #self.ativar_manual()
        #self.sair_conta()

    def construir_login(self):
        self.janela_login=ctk.CTkFrame(self)
        self.janela_login.pack(fill="both",expand=True)

        #==============================================================================================
        #Criando e colocando plano de fundo

        #carregar imagem de fundo
        self.imagem_fundo=ctk.CTkImage(dark_image=Image.open("imagens/PlanoDeFundo/planodefundo.png"),size=(self.winfo_screenwidth(),self.winfo_screenheight()))

        #Criando o fundo
        self.fundo_login=ctk.CTkLabel(self.janela_login,image=self.imagem_fundo,text="")

        #ocupando a tela toda
        self.fundo_login.place(relx=0.5,rely=0.5,anchor="center")


        #==============================================================================================

        #Campo Norte criado
        #campo criado para titulos e logo
        self.campo_norte=ctk.CTkFrame(self.janela_login,fg_color="transparent")
        self.campo_norte.pack(side="top",pady=(220,0))

        self.Campo_texto_Marca=ctk.CTkLabel(self.campo_norte,text="Solar",font=ctk.CTkFont(size=64),text_color="white")
        self.Campo_texto_Marca.pack(pady=(0,120)) #padding apenas no sul

        #==============================================================================================

        #Campo Central
        #campo para centralizar tudo
        self.campo_central=ctk.CTkFrame(self.janela_login,fg_color="transparent")
        self.campo_central.place(relx=0.5,rely=0.4,anchor="center")

        #campo de texto usuario
        self.Campo_nome=ctk.CTkEntry(self.campo_central,placeholder_text="Usuario",width=400,height=50,font=ctk.CTkFont(size=16))
        self.Campo_nome.pack(pady=(0,5))

        #campo de senha usuario
        self.Campo_senha=ctk.CTkEntry(self.campo_central,placeholder_text="Senha",width=400,height=50,font=ctk.CTkFont(size=16))
        self.Campo_senha.pack(pady=(0,5))

        #botao entrar
        self.Botao_Entrar=ctk.CTkButton(self.campo_central,command=self.verificar_login,text="Entrar",text_color="black",fg_color="white",hover_color="black",width=400,height=50,bg_color="transparent",border_color="black")
        self.Botao_Entrar.pack()

        self.Texto_NaoTemConta=ctk.CTkLabel(self.campo_central,text="Não possui uma conta?")
        self.Texto_NaoTemConta.pack()
        
        self.Botao_CriarConta=ctk.CTkButton(self.campo_central,text="Criar",text_color="black",fg_color="white",hover_color="black",width=400,height=50)
        self.Botao_CriarConta.pack(pady=(0,0))

        #================================================================================================

        #Campo Sul
        #self.campo_sul=ctk.CTkFrame(self.janela_login,fg_color="transparent")
        #self.campo_sul.place(relx=0.5, rely=0.65, anchor="center")

        #self.Texto_NaoTemConta=ctk.CTkLabel(self.campo_sul,text="Não possui uma conta?")
        #self.Texto_NaoTemConta.pack()

        #self.Botao_CriarConta=ctk.CTkButton(self.campo_sul,text="Criar",text_color="black",fg_color="white",hover_color="black",width=400,height=50)
        #self.Botao_CriarConta.pack(pady=(0,0))

        #===============================================================================================

    def Criar_Conta(self):
        pass

    def tela_principal(self):
        self.janela_principal=ctk.CTkFrame(self,fg_color="black")
        self.janela_principal.pack(fill="both",expand=True)

        self.barra_lateral()

        #================================================================
        #Criei uma area principal para aparecer os componentes, conforme mudo os icones
        self.area_principal=ctk.CTkFrame(self.janela_principal)
        self.area_principal.pack(side="left",fill="both",expand=True)

        #chamando o dashboard
        self.dashboard()
    
    def barra_lateral(self):
        #Criei a Barra e defini o tamanho dela
        self.Barra_lateral=ctk.CTkFrame(self.janela_principal,width=200,fg_color="#E9E9E9")
        self.Barra_lateral.pack(side="left",fill="y")

        #============================================================================================
        #Criei um campo para o Norte da barra
        #self.Campo_norte_Barra=ctk.CTkFrame(self.Barra_lateral,fg_color="blue")
        #self.Campo_norte_Barra.pack()

        self.texto_Barra_Norte=ctk.CTkLabel(self.Barra_lateral, text="Solar", text_color="Black",font=ctk.CTkFont(size=15))
        self.texto_Barra_Norte.pack(side="top",pady=(8,0))

        #============================================================================================
        #Criei um campo para o Central da barra


        self.Campo_Central_Barra=ctk.CTkFrame(self.Barra_lateral,fg_color="transparent")
        self.Campo_Central_Barra.pack()

        self.criar_Separador_barra()

        self.Texto_Barra_Central=ctk.CTkLabel(self.Barra_lateral,text="Status",text_color="#787878",font=ctk.CTkFont(size=15))
        self.Texto_Barra_Central.pack(pady=(0,5))
        #============================================================================================
        #Load da imagem icone do botao, configuração do botao e setagem dele

        self.icone_dashboard=ctk.CTkImage(dark_image=Image.open("imagens/icones/dashh.png"),size=(18,18))
        self.botao_dashboard=ctk.CTkButton(self.Barra_lateral,text="DashBoard",width=190,height=36,anchor="w",corner_radius=10,border_spacing=12,fg_color="#E9E9E9",hover_color="#FFFFFF",text_color="#292929",font=ctk.CTkFont(size=13),image=self.icone_dashboard,command=lambda: self.troca_tela("DashBoard"))
        self.botao_dashboard.pack(pady=5)

        #============================================================================================
        #Load da imagem icone do botao, configuração do botao e setagem dele
        self.icone_diagnostico=ctk.CTkImage(dark_image=Image.open("imagens/icones/diagnostc.png"),size=(18,18))
        self.botao_diagnostico=ctk.CTkButton(self.Barra_lateral,text="Diagnostico",width=190,height=36,anchor="w",corner_radius=10,border_spacing=12,fg_color="#E9E9E9",hover_color="#FFFFFF",text_color="#292929" ,font=ctk.CTkFont(size=13),image=self.icone_diagnostico, command=lambda: self.troca_tela("Diagnosticos"))
        self.botao_diagnostico.pack(pady=5)

        #============================================================================================
        #Load da imagem icone do botao, configuração do botao e setagem dele
        self.icone_relatorio=ctk.CTkImage(dark_image=Image.open("imagens/icones/relatory.png"),size=(18,18))
        self.botao_relatorio=ctk.CTkButton(self.Barra_lateral,text="Relatorio",width=190,height=36,anchor="w",corner_radius=10,border_spacing=12,fg_color="#E9E9E9",hover_color="#FFFFFF",text_color="#292929" ,font=ctk.CTkFont(size=13),image=self.icone_relatorio)
        self.botao_relatorio.pack(pady=5)

        #============================================================================================
        #Load da imagem icone do botao, configuração do botao e setagem dele
        self.icone_Configuracoes=ctk.CTkImage(dark_image=Image.open("imagens/icones/settings.png"),size=(18,18))
        self.botao_Configuracoes=ctk.CTkButton(self.Barra_lateral,text="Configurações",width=190,height=36,anchor="w",corner_radius=10,border_spacing=12,fg_color="#E9E9E9",hover_color="#FFFFFF",text_color="#292929" ,font=ctk.CTkFont(size=13),image=self.icone_Configuracoes)
        self.botao_Configuracoes.pack(pady=5)

        #============================================================================================
        #Criei um campo para o Sul da barra
        self.Campo_Sul_Barra=ctk.CTkFrame(self.Barra_lateral,fg_color="transparent")
        self.Campo_Sul_Barra.pack()
        self.criar_Separador_barra()


        #============================================================================================
        #Load da imagem icone do botao, configuração do botao e setagem dele
        self.icone_Sair=ctk.CTkImage(dark_image=Image.open("imagens/icones/sair.png"),size=(18,18))
        self.botao_Sair=ctk.CTkButton(self.Barra_lateral,text="Sair",width=80,height=30,fg_color="#E3E3E3",hover_color="#FFFFFF",text_color="#292929",corner_radius=12,command=self.sair_conta,image=self.icone_Sair)
        self.botao_Sair.pack(pady=5)

    def dashboard(self):
        self.tela_dashboard=ctk.CTkFrame(self.area_principal)
        self.tela_dashboard.pack(fill="both",expand=True)

        #================================================================
        #configurando as colunas
        self.tela_dashboard.grid_columnconfigure(0, weight=1)
        self.tela_dashboard.grid_columnconfigure(1, weight=1)

        #================================================================
        #configurando as linhas
        self.tela_dashboard.grid_rowconfigure(0, weight=1)
        self.tela_dashboard.grid_rowconfigure(1, weight=1)

        #================================================================
        #Criei os grids

        self.quadro_1Dash=ctk.CTkFrame(self.tela_dashboard,fg_color="#E9E9E9")
        self.quadro_1Dash.grid(row=0,column=0,padx=10,pady=10, sticky="nsew")

        self.quadro_2Dash=ctk.CTkFrame(self.tela_dashboard,fg_color="#E9E9E9")
        self.quadro_2Dash.grid(row=0,column=1,padx=10,pady=10, sticky="nsew")

        self.quadro_3Dash=ctk.CTkFrame(self.tela_dashboard,fg_color="#E9E9E9")
        self.quadro_3Dash.grid(row=1,column=0,padx=10,pady=10, sticky="nsew")

        self.quadro_4Dash=ctk.CTkFrame(self.tela_dashboard,fg_color="#E9E9E9")
        self.quadro_4Dash.grid(row=1,column=1,padx=10,pady=10, sticky="nsew")

        #================================================================
        #Inserção dos dados nos seus respectivos quadrantes
        #Quadrante 1
        self.Geracao_Potencia=ctk.CTkLabel(self.quadro_1Dash,text="Geração de Energia (W)",font=ctk.CTkFont(size=50))
        self.valor_Potencia=ctk.CTkLabel(self.quadro_1Dash,text="0.0 W",font=ctk.CTkFont(size=30))

        self.Geracao_Potencia.pack()
        self.valor_Potencia.pack()

        #================================================================
        #Inserção dos dados nos seus respectivos quadrantes
        #Quadrante 2

        self.angulo180=ctk.CTkLabel(self.quadro_2Dash, text="Angulo do Servo: 0°",font=ctk.CTkFont(size=50))
        self.angulo360=ctk.CTkLabel(self.quadro_2Dash, text="Angulo do motor de Passo: 0°",font=ctk.CTkFont(size=30))

        self.angulo180.pack()
        self.angulo360.pack()

        #================================================================
        #Inserção dos dados nos seus respectivos quadrantes
        #Quadrante 3

        self.Luminosidade_Cruz1=ctk.CTkLabel(self.quadro_3Dash,text="Luminosidade do LDR 1:",font=ctk.CTkFont(size=20))
        self.Luminosidade_Cruz2=ctk.CTkLabel(self.quadro_3Dash,text="Luminosidade do LDR 2:",font=ctk.CTkFont(size=20))
        self.Luminosidade_Cruz3=ctk.CTkLabel(self.quadro_3Dash,text="Luminosidade do LDR 3:",font=ctk.CTkFont(size=20))
        self.Luminosidade_Cruz4=ctk.CTkLabel(self.quadro_3Dash,text="Luminosidade do LDR 4:",font=ctk.CTkFont(size=20))

        self.Luminosidade_Cruz1.pack()
        self.Luminosidade_Cruz2.pack()
        self.Luminosidade_Cruz3.pack()
        self.Luminosidade_Cruz4.pack()

        #================================================================
        #Inserção dos dados nos seus respectivos quadrantes
        #Quadrante 4

        self.botao_automatico=ctk.CTkButton(self.quadro_4Dash,text="Modo Automatico",text_color="black",fg_color="white",hover_color="black",width=400,height=50)
        self.botao_automatico.pack(pady=10)

        self.botao_manual=ctk.CTkButton(self.quadro_4Dash,text="Modo manual",text_color="black",fg_color="white",hover_color="black",width=400,height=50)
        self.botao_manual.pack(pady=10)

    def diagnosticos(self):
        self.tela_diagnosticos=ctk.CTkFrame(self.area_principal)
        self.tela_diagnosticos.pack(fill="both",expand=True)


        #================================================================
        #configurando as colunas
        self.tela_diagnosticos.grid_columnconfigure(0,weight=1)
        self.tela_diagnosticos.grid_columnconfigure(1, weight=1)

        #================================================================
        #configurando as linhas
        self.tela_diagnosticos.grid_rowconfigure(0, weight=1)

        self.quadro_1Diag=ctk.CTkFrame(self.tela_diagnosticos,fg_color="#E9E9E9")
        #self.Calibracao_Titulo=ctk.CTkLabel(self.quadro_1Diag,text="Calibração",font=ctk.CTkFont(size=30))
        #self.Calibracao_Titulo.pack()

        self.quadro_1Diag.grid(row=0,column=0,padx=10,pady=10, sticky="nsew")
        
        self.quadro_2Diag=ctk.CTkFrame(self.tela_diagnosticos, fg_color="#E9E9E9")
        self.quadro_2Diag.grid(row=0,column=1,padx=10,pady=10, sticky="nsew")

        #Acima são os dois quadrantes principais (esquerda e direita)
        #================================================================


        #================================================================
        #Abaixo são os subquadrantes dentro do quadro_1

        self.quadro_1Diag.grid_columnconfigure(0,weight=1)
        self.quadro_1Diag.grid_columnconfigure(1, weight=1)

        self.quadro_1Diag.grid_rowconfigure(0, weight=1)
        #================================================================
        
        self.subquadro_1=ctk.CTkFrame(self.quadro_1Diag,height=250,width=120,fg_color="#FFFEFE")
        self.subquadro_1.grid(row=0,column=0, padx=10, pady=10)

        self.subquadro__2=ctk.CTkFrame(self.quadro_1Diag,height=250,width=120,fg_color="#FFFEFE")
        self.subquadro__2.grid(row=0, column=1,padx=10,pady=10)
        

        #================================================================
        #Dados referente ao Motor de Passo
        self.Calibracao_Motor=ctk.CTkFrame(self.subquadro_1)
    
        self.Motor_dePassoTexto=ctk.CTkLabel(self.subquadro_1,text="Motor de passo",text_color="black",font=ctk.CTkFont(size=25))
        self.Motor_dePassoTexto.pack()

        self.Motor_dePassoSubTexto=ctk.CTkLabel(self.subquadro_1,text="Retorna ao ponto zero",text_color="black",font=ctk.CTkFont(size=15))
        self.Motor_dePassoSubTexto.pack()

        self.Motor_dePassoBarr=ctk.CTkProgressBar(self.subquadro_1, width=400)
        self.Motor_dePassoBarr.pack()

        self.Calibracao_Motor=ctk.CTkButton(self.subquadro_1,width=100, height=20,text="Calibrar Motor",font=ctk.CTkFont(size=18),fg_color="transparent",hover_color="Black",text_color="#B3B3B3",)
        self.Calibracao_Motor.pack(pady=10)

        #================================================================
        #Dados referente ao Servo Motor
        self.Motor_ServoTexto=ctk.CTkLabel(self.subquadro__2,text="Motor Servo",text_color="black",font=ctk.CTkFont(size=25))
        self.Motor_ServoTexto.pack()
        
        self.Motor_ServoSubTexto=ctk.CTkLabel(self.subquadro__2,text="Retorna ao angulo Inicial",text_color="black",font=ctk.CTkFont(size=15))
        self.Motor_ServoSubTexto.pack()
        
        self.Motor_ServoBarr=ctk.CTkProgressBar(self.subquadro__2, width=400)
        self.Motor_ServoBarr.pack()

        self.Calibracao_Servo=ctk.CTkButton(self.subquadro__2,width=100,height=20,text="Calibrar Servo",font=ctk.CTkFont(size=18),fg_color="transparent",hover_color="Black",text_color="#B3B3B3")
        self.Calibracao_Servo.pack(pady=10)

    def relatorios(self):
        pass

    def configuracoes(self):
        pass

#=================================================================================
#=================================Acima front end=================================
#=================================Abaixo Esteticas Extras=========================
#=================================================================================

    def criar_Separador_barra(self):
        self.separador=ctk.CTkFrame(self.Barra_lateral,height=3,corner_radius=0,fg_color="#E3E3E3")
        self.separador.pack(fill="x",padx=12,pady=15)

#=================================================================================
#=================================Acima Esteticas Extras==========================
#=================================Abaixo BackEnd==================================
#=================================================================================

    def verificar_login(self):
        usuario= self.Campo_nome.get()
        senha= self.Campo_senha.get()

        if usuario == self.usuario_login and senha== self.usuario_senha:
            self.janela_login.destroy()
            self.tela_principal()
        else:
            print("Nome ou senha incorreto")

    def troca_tela(self,tela):
        for widget in self.area_principal.winfo_children():
            widget.destroy()

        if tela=="DashBoard":
            self.dashboard()
            print("deu certo")

        elif tela=="Diagnosticos":
            self.diagnosticos()
            print("Deu certo Diagnosticos")

        elif tela=="Relatorios":
            self.relatorios()

        elif tela=="configuracoes":
            self.configuracoes()


    #def ativar_automatico(self):
        #self.arduino.write(b'A')

    #def ativar_manual(self):
        #self.arduino.write(b'M')

    def sair_conta(self):
        self.janela_principal.destroy()
        self.construir_login()

janela=aplicativo()
janela.mainloop()