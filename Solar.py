#Nome: Vinicius de Moraes Regis
#Projeto: Painel Solar que segue a Luz em 180° e 360°
#Data de Criação: 10/10/2026
#Projeto que Criei para um sistema de painel solar que segue a luz 360° com um Motor de Passo e 180° com um Servo Motor
#Estou usando um Arduino simplesmente pela facilidade de só conectar no PC e ter o front-end
#

import customtkinter as ctk
from PIL import Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
from matplotlib.patches import Wedge

import random
from datetime import datetime
from collections import deque

import serial

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        #self.arduino=serial.Serial("COM3",9600,timeout=1)

        self.title("Solar")
        self.attributes("-fullscreen",True)

        self.usuario_login="1"
        self.usuario_senha="1"


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

        self.Campo_texto_Marca=ctk.CTkLabel(self.campo_norte,text="Solar",text_color="white",font=ctk.CTkFont(size=60,family="Segoe UI",weight="bold"))
        self.Campo_texto_Marca.pack(pady=(0,120)) #padding apenas no sul

        #==============================================================================================

        #Campo Central
        #campo para centralizar tudo
        self.campo_central=ctk.CTkFrame(self.janela_login,fg_color="transparent")
        self.campo_central.place(relx=0.5,rely=0.4,anchor="center")

        #campo de texto usuario
        self.Campo_nome=ctk.CTkEntry(self.campo_central,placeholder_text="Usuario",width=400,height=50,font=ctk.CTkFont(size=16),corner_radius=25,placeholder_text_color="#e8e8e8",border_width=0)
        self.Campo_nome.pack(pady=(0,5))

        #campo de senha usuario
        self.Campo_senha=ctk.CTkEntry(self.campo_central,placeholder_text="Senha",width=400,height=50,font=ctk.CTkFont(size=16),corner_radius=25,placeholder_text_color="#e8e8e8",border_width=0,show="*")
        self.Campo_senha.pack(pady=(0,5))

        #botao entrar
        self.Botao_Entrar=ctk.CTkButton(self.campo_central,command=self.verificar_login,text="Entrar",text_color="black",fg_color="#E9E9E9",hover_color="#FFFFFF",width=400,height=50,bg_color="transparent",border_color="black",corner_radius=25)
        self.Botao_Entrar.pack(pady=(0,15))

        self.Texto_NaoTemConta=ctk.CTkLabel(self.campo_central,text="Não possui uma conta?")
        self.Texto_NaoTemConta.pack()
        
        self.Botao_CriarConta=ctk.CTkButton(self.campo_central,text="Criar",text_color="black",fg_color="transparent",hover_color="#FFFFFF",width=400,height=50,corner_radius=25)
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

        self.texto_Barra_Norte=ctk.CTkLabel(self.Barra_lateral, text="Solar", text_color="#e1e1e1",font=ctk.CTkFont(size=15,family="Segoe UI",weight="bold"))
        self.texto_Barra_Norte.pack(side="top",pady=(8,0))

        #============================================================================================
        #Criei um campo para o Central da barra


        self.Campo_Central_Barra=ctk.CTkFrame(self.Barra_lateral,fg_color="transparent")
        self.Campo_Central_Barra.pack(side="top",fill="x")

        self.criar_Separador_barra()

        self.Texto_Barra_Central=ctk.CTkLabel(self.Barra_lateral,text="Status",text_color="#787878",font=ctk.CTkFont(size=15))
        self.Texto_Barra_Central.pack(pady=(0,5))
        #============================================================================================
        #Load da imagem icone do botao, configuração do botao e setagem dele

        self.icone_dashboard=ctk.CTkImage(dark_image=Image.open("imagens/IconesBarraLateral/dashh.png"),size=(18,18))
        self.botao_dashboard=ctk.CTkButton(self.Barra_lateral,text="DashBoard",width=190,height=36,anchor="w",corner_radius=10,border_spacing=12,fg_color="#E9E9E9",hover_color="#FFFFFF",text_color="#292929",font=ctk.CTkFont(size=13),image=self.icone_dashboard,command=lambda: self.troca_tela("DashBoard"))
        self.botao_dashboard.pack(pady=5)

        #============================================================================================
        #Load da imagem icone do botao, configuração do botao e setagem dele
        self.icone_diagnostico=ctk.CTkImage(dark_image=Image.open("imagens/IconesBarraLateral/diagnostc.png"),size=(18,18))
        self.botao_diagnostico=ctk.CTkButton(self.Barra_lateral,text="Diagnostico",width=190,height=36,anchor="w",corner_radius=10,border_spacing=12,fg_color="#E9E9E9",hover_color="#FFFFFF",text_color="#292929" ,font=ctk.CTkFont(size=13),image=self.icone_diagnostico, command=lambda: self.troca_tela("Diagnosticos"))
        self.botao_diagnostico.pack(pady=5)

        #============================================================================================
        #Load da imagem icone do botao, configuração do botao e setagem dele
        self.icone_relatorio=ctk.CTkImage(dark_image=Image.open("imagens/IconesBarraLateral/relatory.png"),size=(18,18))
        self.botao_relatorio=ctk.CTkButton(self.Barra_lateral,text="Relatorio",width=190,height=36,anchor="w",corner_radius=10,border_spacing=12,fg_color="#E9E9E9",hover_color="#FFFFFF",text_color="#292929" ,font=ctk.CTkFont(size=13),image=self.icone_relatorio,command=lambda: self.troca_tela("Relatorios"))
        self.botao_relatorio.pack(pady=5)

        #============================================================================================
        #Load da imagem icone do botao, configuração do botao e setagem dele
        self.icone_Configuracoes=ctk.CTkImage(dark_image=Image.open("imagens/IconesBarraLateral/settings.png"),size=(18,18))
        self.botao_Configuracoes=ctk.CTkButton(self.Barra_lateral,text="Configurações",width=190,height=36,anchor="w",corner_radius=10,border_spacing=12,fg_color="#E9E9E9",hover_color="#FFFFFF",text_color="#292929" ,font=ctk.CTkFont(size=13),image=self.icone_Configuracoes)
        self.botao_Configuracoes.pack(pady=5)

        #============================================================================================
        #Criei um campo para o Sul da barra
        self.Campo_Sul_Barra=ctk.CTkFrame(self.Barra_lateral,fg_color="transparent")
        self.Campo_Sul_Barra.pack(side="bottom",fill="x",pady=10)
        self.criar_Separador_barra()


        #============================================================================================
        #Load da imagem icone do botao, configuração do botao e setagem dele
        self.icone_Sair=ctk.CTkImage(dark_image=Image.open("imagens/IconesBarraLateral/sair.png"),size=(18,18))
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

        self.PrimeiroQuadranteDashboard=ctk.CTkFrame(self.quadro_1Dash,fg_color="#E9E9E9")
        self.PrimeiroQuadranteDashboard.pack(expand=True)

        self.Geracao_Potencia=ctk.CTkLabel(self.PrimeiroQuadranteDashboard,text="Geração de Energia (W)",font=ctk.CTkFont(size=15,family="Segoe UI",weight="bold"))
        self.Geracao_PotenciaSubTitulo=ctk.CTkLabel(self.PrimeiroQuadranteDashboard,text="INA219",font=ctk.CTkFont(size=10))
        self.valor_Potencia=ctk.CTkLabel(self.PrimeiroQuadranteDashboard,text="5.0 mW",font=ctk.CTkFont(size=45))

        #================================================================
        #Dados da potência

        self.Geracao_Potencia.pack(pady=10)
        self.Geracao_PotenciaSubTitulo.pack()
        self.valor_Potencia.pack()

        self.horariosGraficoPlot = deque(maxlen=30)
        self.potenciaGraficoPlot = deque(maxlen=30)


        #================================================================
        #Criando a figura

        self.figuraPlot = Figure(figsize=(8, 2), dpi=100)
        self.figuraPlot.patch.set_facecolor("#E9E9E9")


        #================================================================
        #Criando o gráfico

        self.graficoPlot = self.figuraPlot.add_subplot(111)
        self.graficoPlot.set_facecolor("#E9E9E9")


        #Removi as grades e os eixos para que ficasse clean

        self.graficoPlot.grid(False)
        self.graficoPlot.set_axis_off()


        #================================================================
        #Criei a linha de potencia

        self.linha_graficoPlot, = self.graficoPlot.plot([],[],color="#555555",linewidth=2)
        #================================================================
        #inseri o grafico dentro do quadrante 1

        self.canvas_graficoPlot = FigureCanvasTkAgg(self.figuraPlot,master=self.PrimeiroQuadranteDashboard)

        self.canvas_graficoPlot.get_tk_widget().pack(fill="x",expand=True,padx=10,pady=10)


        # Iniciando a atualização
        self.atualizar_graficoPlot()
        #================================================================
        self.Quadros_PrimeiroQuadrante=ctk.CTkFrame(self.PrimeiroQuadranteDashboard,fg_color="#E9E9E9",height=350,width=600)
        self.Quadros_PrimeiroQuadrante.pack(expand=True)
        self.Quadros_PrimeiroQuadrante.pack_propagate(False)
        #================================================================
        #Primeiro bloco do Quadrante 1, marcando a tensao
        self.quadro_1x1Dash=ctk.CTkFrame(self.Quadros_PrimeiroQuadrante,fg_color="#E9E9E9")
        self.quadro_1x1Dash.grid(row=0,column=0,pady=(0,5))

        self.Bloco_1x1Dash=ctk.CTkFrame(self.quadro_1x1Dash,fg_color="#E9E9E9",height=50,width=150)
        self.TextoBloco_1x1Dash=ctk.CTkLabel(self.Bloco_1x1Dash,text="Tensão:",text_color="#bdbdbd",font=ctk.CTkFont(size=15,family="Segoe UI",weight="bold"))
        self.SubTextoBloco_1x1Dash=ctk.CTkLabel(self.Bloco_1x1Dash,text="0V",text_color="#6e6e6e",font=ctk.CTkFont(size=25,family="Segoe UI",weight="bold"))
        self.Bloco_1x1Dash.pack(padx=3)
        self.Bloco_1x1Dash.pack_propagate(False)
        self.TextoBloco_1x1Dash.pack()
        self.SubTextoBloco_1x1Dash.pack()

        #================================================================
        #Segundo bloco do Quadrante 1
        self.quadro_1x2Dash=ctk.CTkFrame(self.Quadros_PrimeiroQuadrante,fg_color="#E9E9E9")
        self.quadro_1x2Dash.grid(row=0,column=1,pady=(0,5))

        self.Bloco_1x2Dash=ctk.CTkFrame(self.quadro_1x2Dash,fg_color="#E9E9E9",height=50,width=150)
        self.TextoBloco_1x2Dash=ctk.CTkLabel(self.Bloco_1x2Dash,text="Tensao Shunt:",text_color="#bdbdbd",font=ctk.CTkFont(size=15,family="Segoe UI",weight="bold"))
        self.SubTextoBloco_1x2Dash=ctk.CTkLabel(self.Bloco_1x2Dash,text="0mV",text_color="#6e6e6e",font=ctk.CTkFont(size=25,family="Segoe UI",weight="bold"))
        self.Bloco_1x2Dash.pack(padx=3)
        self.Bloco_1x2Dash.pack_propagate(False)
        self.TextoBloco_1x2Dash.pack()
        self.SubTextoBloco_1x2Dash.pack()

        #================================================================
        #terceiro bloco do Quadrante 1
        self.quadro_1x3Dash=ctk.CTkFrame(self.Quadros_PrimeiroQuadrante,fg_color="#E9E9E9")
        self.quadro_1x3Dash.grid(row=0,column=2,pady=(0,5))

        self.Bloco_1x3Dash=ctk.CTkFrame(self.quadro_1x3Dash,fg_color="#E9E9E9",height=50,width=150)
        self.TextoBloco_1x3Dash=ctk.CTkLabel(self.Bloco_1x3Dash,text="Corrente:",text_color="#bdbdbd",font=ctk.CTkFont(size=15,family="Segoe UI",weight="bold"))
        self.SubTextoBloco_1x3Dash=ctk.CTkLabel(self.Bloco_1x3Dash,text="0A",text_color="#6e6e6e",font=ctk.CTkFont(size=25,family="Segoe UI",weight="bold"))
        self.Bloco_1x3Dash.pack(padx=3)
        self.Bloco_1x3Dash.pack_propagate(False)
        self.TextoBloco_1x3Dash.pack()
        self.SubTextoBloco_1x3Dash.pack()

        #================================================================
        #Quarto bloco do Quadrante 1
        self.quadro_1x4Dash=ctk.CTkFrame(self.Quadros_PrimeiroQuadrante,fg_color="#E9E9E9")
        self.quadro_1x4Dash.grid(row=0,column=3,pady=(0,0))

        self.Bloco_1x4Dash=ctk.CTkFrame(self.quadro_1x4Dash,fg_color="#E9E9E9",height=50,width=150)
        self.TextoBloco_1x4Dash=ctk.CTkLabel(self.Bloco_1x4Dash,text="Potência:",text_color="#bdbdbd",font=ctk.CTkFont(size=15,family="Segoe UI",weight="bold"))
        self.SubTextoBloco_1x4Dash=ctk.CTkLabel(self.Bloco_1x4Dash,text="0W",text_color="#6e6e6e",font=ctk.CTkFont(size=25,family="Segoe UI",weight="bold"))
        self.Bloco_1x4Dash.pack(padx=3)
        self.Bloco_1x4Dash.pack_propagate(False)
        self.TextoBloco_1x4Dash.pack()
        self.SubTextoBloco_1x4Dash.pack()

        #================================================================
        #Inserção dos dados nos seus respectivos quadrantes
        #Quadrante 2
        self.SegundoQuadranteDashboard=ctk.CTkFrame(self.quadro_2Dash,fg_color="#E9E9E9")
        self.SegundoQuadranteDashboard.pack(expand=True)

        self.Texto_Angulacao=ctk.CTkLabel(self.SegundoQuadranteDashboard,text="Angulação dos Motores",font=ctk.CTkFont(size=30,family="Segoe UI",weight="bold"))
        self.Texto_Angulacao.pack(pady=(0,5))

        #Quantos graus o motor de passo e o servo motor estão 
        self.angulo180=ctk.CTkLabel(self.SegundoQuadranteDashboard, text="Angulo do Servo: 0°",font=ctk.CTkFont(size=15))
        self.angulo360=ctk.CTkLabel(self.SegundoQuadranteDashboard, text="Angulo do motor de Passo: 0°",font=ctk.CTkFont(size=15))

        self.angulo180.pack(pady=(0,5))
        self.angulo360.pack(pady=(0,5))
        
        #================================================================
        #Inserção dos dados nos seus respectivos quadrantes
        #Quadrante 3
        self.Texto_TituloLuminosidadeLDRCruz=ctk.CTkLabel(self.quadro_3Dash,text="Lumens",font=ctk.CTkFont(size=30,family="Segoe UI",weight="bold"))
        self.Texto_TituloLuminosidadeLDRCruz.pack(pady=(10,1))

        self.Texto_subTituloLuminosidadeLDRCruz=ctk.CTkLabel(self.quadro_3Dash,text="Quantidade de lúmens incidindo na Cruz",font=ctk.CTkFont(size=10))
        self.Texto_subTituloLuminosidadeLDRCruz.pack(pady=(0,14))

        #Os LDRS devem ser os que ficam na cruz, não os da base
        self.Luminosidade_Cruz1=ctk.CTkLabel(self.quadro_3Dash,text="Luminosidade do LDR 1:",font=ctk.CTkFont(size=20))
        self.Luminosidade_Cruz2=ctk.CTkLabel(self.quadro_3Dash,text="Luminosidade do LDR 2:",font=ctk.CTkFont(size=20))
        self.Luminosidade_Cruz3=ctk.CTkLabel(self.quadro_3Dash,text="Luminosidade do LDR 3:",font=ctk.CTkFont(size=20))
        self.Luminosidade_Cruz4=ctk.CTkLabel(self.quadro_3Dash,text="Luminosidade do LDR 4:",font=ctk.CTkFont(size=20))


        self.Luminosidade_Cruz1.pack(pady=(0,6))
        self.Luminosidade_Cruz2.pack(pady=(0,6))
        self.Luminosidade_Cruz3.pack(pady=(0,6))
        self.Luminosidade_Cruz4.pack(pady=(0,6))

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
        self.Calibracao_Titulo=ctk.CTkLabel(self.quadro_1Diag,text="Calibração",font=ctk.CTkFont(size=30,family="Segoe UI",weight="bold"))
        self.Calibracao_Titulo.pack(pady=10)

        self.quadro_1Diag.grid(row=0,column=0,padx=10,pady=10, sticky="nsew")
        
        self.quadro_2Diag=ctk.CTkFrame(self.tela_diagnosticos, fg_color="#E9E9E9")
        
        self.quadro_2Diag.grid(row=0,column=1,padx=10,pady=10, sticky="nsew")

        #Acima são os dois quadrantes principais (esquerda e direita)

        #================================================================
        #================================================================
        #========================ABA ESQUERDA============================
        #Frame Criado para guardar dados do Servo e do Motor de Passo
        self.Calibracao_Motor=ctk.CTkFrame(self.quadro_1Diag,fg_color="#E9E9E9")
        self.Calibracao_Motor.pack(fill="x",padx=20)

        self.Status_doSistemaFrame=ctk.CTkFrame(self.quadro_2Diag,fg_color="#E9E9E9")
        self.Status_doSistemaFrame.pack(fill="both",expand=True)

        self.criar_SeparadorAbaCalibracao()
        #================================================================
        #Dados referente ao Motor de Passo
        self.Frame_MotordePasso=ctk.CTkFrame(self.Calibracao_Motor,fg_color="#E9E9E9",height=150,border_color="#E1E1E1",border_width=3)
        self.Frame_MotordePasso.pack(fill="x",expand=True,pady=10)
        self.Frame_MotordePasso.pack_propagate(False)

        self.Motor_dePassoTexto=ctk.CTkLabel(self.Frame_MotordePasso,text="Motor de passo",text_color="black",font=ctk.CTkFont(size=25,family="Segoe UI",weight="bold"))
        self.Motor_dePassoTexto.pack(pady=(5,0))

        self.Motor_dePassoSubTexto=ctk.CTkLabel(self.Frame_MotordePasso,text="Retorna ao ponto zero",text_color="black",font=ctk.CTkFont(size=15))
        self.Motor_dePassoSubTexto.pack()

        self.Motor_dePassoBarr=ctk.CTkProgressBar(self.Frame_MotordePasso, width=350,progress_color="#E1E1E1")
        self.Motor_dePassoBarr.pack(pady=(30,0))

        self.Botao_Calibracao_Motor=ctk.CTkButton(self.Frame_MotordePasso,width=150, height=40,text="Calibrar Motor",font=ctk.CTkFont(size=18),fg_color="transparent",hover_color="#FFFFFF",text_color="#B3B3B3",)
        self.Botao_Calibracao_Motor.pack(pady=10)

        #================================================================
        #Dados referente ao Servo Motor

        self.Frame_MotorServo=ctk.CTkFrame(self.Calibracao_Motor, fg_color="#E9E9E9", height=150,border_color="#E1E1E1",border_width=3)
        self.Frame_MotorServo.pack(fill="x",expand=True,pady=10)
        self.Frame_MotorServo.pack_propagate(False)

        self.Motor_ServoTexto=ctk.CTkLabel(self.Frame_MotorServo,text="Motor Servo",text_color="black",font=ctk.CTkFont(size=25,family="Segoe UI",weight="bold"))
        self.Motor_ServoTexto.pack(pady=(5,0))
        
        self.Motor_ServoSubTexto=ctk.CTkLabel(self.Frame_MotorServo,text="Retorna ao angulo Inicial",text_color="black",font=ctk.CTkFont(size=15))
        self.Motor_ServoSubTexto.pack()
        
        self.Motor_ServoBarr=ctk.CTkProgressBar(self.Frame_MotorServo, width=350,progress_color="#E1E1E1")
        self.Motor_ServoBarr.pack(pady=(30,0))

        self.Calibracao_Servo=ctk.CTkButton(self.Frame_MotorServo,width=150,height=40,text="Calibrar Servo",font=ctk.CTkFont(size=18),fg_color="transparent",hover_color="#FFFFFF",text_color="#B3B3B3")
        self.Calibracao_Servo.pack(pady=10)

        self.criar_SeparadorAbaCalibracao()

        #================================================================
        #Referencias dos eixos

        self.referencia_eixos=ctk.CTkFrame(self.Calibracao_Motor,fg_color="#E9E9E9",height=400)
        self.referencia_eixos.pack(fill="x",expand=True,pady=10)

        self.Texto_TituloReferenciaDosEixos=ctk.CTkLabel(self.referencia_eixos,text="Referência dos Eixos",font=ctk.CTkFont(size=25,family="Segoe UI",weight="bold"))
        self.Texto_TituloReferenciaDosEixos.pack(pady=(0,20))

        self.Texto_ReferenciaEixoHorizontal=ctk.CTkLabel(self.referencia_eixos,text="Horizontal:",text_color="black",font=ctk.CTkFont(size=15))
        self.Texto_ReferenciaEixoHorizontal.pack(pady=(0,5))

        self.Texto_ReferenciaEixoVertical=ctk.CTkLabel(self.referencia_eixos,text="Vertical:",text_color="black",font=ctk.CTkFont(size=15))
        self.Texto_ReferenciaEixoVertical.pack(pady=(0,5))
        #================================================================
        #Espaço para eu criar um grafico
        #criei a figura do grafico
        # Criando a figura
        self.figura_motorFatia = Figure(figsize=(4, 4), dpi=100)
        self.figura_motorFatia.patch.set_facecolor("#E9E9E9")

        # Criando a área do gráfico
        self.grafico_motorFatia = self.figura_motorFatia.add_subplot(111)
        self.grafico_motorFatia.set_facecolor("#F5F5F5")
        self.grafico_motorFatia.set_aspect("equal")
        self.grafico_motorFatia.set_xlim(-1.2, 1.2)
        self.grafico_motorFatia.set_ylim(-1.2, 1.2)
        self.grafico_motorFatia.axis("off")

        # Criando o anel cinza de fundo
        self.fundo_motorFatia = Wedge(center=(0, 0),r=1,theta1=0,theta2=360,width=0.25,facecolor="#D0D0D0")
        
        self.grafico_motorFatia.add_patch(self.fundo_motorFatia)

        # Inicializando a fatia que será atualizada
        self.fatia_motor = None

        # Inserindo o gráfico no diagnóstico
        self.canvas_motorFatia = FigureCanvasTkAgg(self.figura_motorFatia,master=self.referencia_eixos)

        self.canvas_motorFatia.get_tk_widget().pack(pady=10)

        # Testando com 90 graus
        self.atualizar_graficoFatia(90)

        #================================================================
        #================================================================
        #========================ABA DIREITA============================
        #Frame Criado para status do sistema
        self.Status_doSistema=ctk.CTkFrame(self.Status_doSistemaFrame,fg_color="transparent")
        self.Status_doSistema.pack()
        #================================================================
        #aqui eu criei o titulo, subtitulo e tambem um frame para a organização dos textos
        self.Status_Titulo=ctk.CTkLabel(self.Status_doSistema,text="Status do Sistema",text_color="black",font=ctk.CTkFont(size=25,family="Segoe UI",weight="bold"))
        self.Status_Titulo.pack()

        self.Status_SubTitulo=ctk.CTkLabel(self.Status_doSistema,text="Atualizado em tempo real",font=ctk.CTkFont(size=15))
        self.Status_SubTitulo.pack()

        self.Status_doSistemaInformacoes=ctk.CTkFrame(self.Status_doSistemaFrame,fg_color="#E9E9E9")
        self.Status_doSistemaInformacoes.pack(fill="both",expand=True,padx=30,pady=(15,30))
        #================================================================
        #Informacoes do Sistema
        #Por conta da repetição de um mesmo modelo de texto, nao tem motivo para eu ficar ocupando linha, decidir criar uma função e dar os dados quando chamar ela
        #criei um outro separador de linha, ja que o da aba de calibração estava setado para ele especificamente
        self.Status_Arduino = self.StatusInfos("Arduino", "Desconectado")

        self.criar_SeparadorAbaStatus()

        self.Status_LDR = self.StatusInfos("Sensores LDR", "Aguardando")

        self.criar_SeparadorAbaStatus()

        self.Status_Motor = self.StatusInfos("Motor de passo", "Em espera")

        self.criar_SeparadorAbaStatus()

        self.Status_Servo = self.StatusInfos("Servomotor", "Em espera")

        self.criar_SeparadorAbaStatus()

        self.Status_Calibracao = self.StatusInfos("Calibração", "Pendente")

    def relatorios(self):
        self.aba_Relatorios=ctk.CTkFrame(self.area_principal)
        self.aba_Relatorios.pack(fill="both",expand=True)

        #Nessa aba eu planejo criar 3 blocos referente à Potencia
        #Energia gerada, Pico de potencia e Tempo de geração
        #Talvez criar um grafico diario?

        self.texto_TituloRelatorio=ctk.CTkLabel(self.aba_Relatorios,text="Relatorios",font=ctk.CTkFont(size=30,family="Segoe UI",weight="bold"))
        self.texto_TituloRelatorio.pack(anchor="w",padx=(10,0),pady=(10,4))

        self.Text_subTituloRelatorio=ctk.CTkLabel(self.aba_Relatorios,text="Historico de desempenho do Painel Solar")
        self.Text_subTituloRelatorio.pack(anchor="w",padx=(10,0))

        #Para nos criarmos os blocos, precisamos criar um novo Frame, pois .Grid e .Pack nao podem compartilhar o mesmo pai "aba_Relatorios"
        self.Armazenar_BlocosRelatorio=ctk.CTkFrame(self.aba_Relatorios,fg_color="#E9E9E9")
        self.Armazenar_BlocosRelatorio.pack(fill="x",padx=6,pady=6)

        #Criando as colunas
        self.Armazenar_BlocosRelatorio.grid_columnconfigure(0, weight=1)
        self.Armazenar_BlocosRelatorio.grid_columnconfigure(1, weight=1)
        self.Armazenar_BlocosRelatorio.grid_columnconfigure(2,weight=1)
        #================================================================
        #Criando os blocos

        self.EnergiaGerada=ctk.CTkFrame(self.Armazenar_BlocosRelatorio,fg_color="#E9E9E9",height=150,width=300)
        self.EnergiaGerada.grid(row=0,column=0, padx=2,pady=5)
        self.EnergiaGerada.grid_propagate(False)

        self.PicoDePotencia=ctk.CTkFrame(self.Armazenar_BlocosRelatorio,fg_color="#E9E9E9",height=150,width=300)
        self.PicoDePotencia.grid(row=0,column=1, padx=2,pady=5)
        self.PicoDePotencia.grid_propagate(False)

        self.TempoDeGeracao=ctk.CTkFrame(self.Armazenar_BlocosRelatorio,fg_color="#E9E9E9",height=150,width=300)
        self.TempoDeGeracao.grid(row=0,column=2, padx=2,pady=5)
        self.TempoDeGeracao.grid_propagate(False)

        #================================================================
        #Dados do Bloco de Energia Gerada
        self.Icone_EnergiaGerada=ctk.CTkImage(dark_image=Image.open("imagens/IconesRelatorios/energiaGerada.png"),size=(18,18))
        self.EnerGiaGerada_Titulo=ctk.CTkLabel(self.EnergiaGerada,image=self.Icone_EnergiaGerada,text="")
        self.EnerGiaGerada_Titulo.pack(anchor="w",padx=(10,0),pady=(5,0))
        self.EnergiaGerada.pack_propagate(False)

        self.EnergiaGerada_subTitulo=ctk.CTkLabel(self.EnergiaGerada,text="Energia gerada",font=ctk.CTkFont(size=18,family="Segoe UI",weight="bold"))
        self.EnergiaGerada_subTitulo.pack(anchor="w",padx=(10,0))
        self.EnergiaGerada_subTitulo.pack_propagate(False)

        self.Valor_EnergiaGerada=ctk.CTkLabel(self.EnergiaGerada,text="0 Wh",font=ctk.CTkFont(size=25,family="Segoe UI",weight="bold"))
        self.Valor_EnergiaGerada.pack(anchor="w",padx=(10,0),pady=(8,0))
        self.Valor_EnergiaGerada.pack_propagate(False)

        #================================================================
        #Dados do Bloco de Pico de Potencia
        self.Icone_PicoPotencia=ctk.CTkImage(dark_image=Image.open("imagens/IconesRelatorios/seta.png"),size=(18,18))
        self.Icone_PicoPotencia_Titulo=ctk.CTkLabel(self.PicoDePotencia,image=self.Icone_PicoPotencia)
        self.Icone_PicoPotencia_Titulo.pack(anchor="w",padx=(10,0),pady=(5,0))
        self.PicoDePotencia.pack_propagate(False)

        self.PicoDePotencia_subTitulo=ctk.CTkLabel(self.PicoDePotencia,text="Pico de Potência",font=ctk.CTkFont(size=18,family="Segoe UI",weight="bold"))
        self.PicoDePotencia_subTitulo.pack(anchor="w", padx=(10,10))
        self.PicoDePotencia_subTitulo.pack_propagate(False)

        self.Valor_PicoDePotencia=ctk.CTkLabel(self.PicoDePotencia,text="0 Wh",font=ctk.CTkFont(size=25,family="Segoe UI",weight="bold"))
        self.Valor_PicoDePotencia.pack(anchor="w",padx=(10,0),pady=(8,0))
        self.Valor_PicoDePotencia.pack_propagate(False)

        #================================================================
        #Dados do Bloco de Tempo de Geração

        self.Icone_TempoGeracao=ctk.CTkImage(dark_image=Image.open("imagens/IconesRelatorios/RELOGIO.png"),size=(18,18))
        self.Icone_TempoGeracao_Titulo=ctk.CTkLabel(self.TempoDeGeracao,image=self.Icone_TempoGeracao)
        self.Icone_TempoGeracao_Titulo.pack(anchor="w",padx=(10,0),pady=(5,0))
        self.TempoDeGeracao.pack_propagate(False)
        
        self.TempoGeracao_subTitulo=ctk.CTkLabel(self.TempoDeGeracao,text="Pico de Potência",font=ctk.CTkFont(size=18,family="Segoe UI",weight="bold"))
        self.TempoGeracao_subTitulo.pack(anchor="w", padx=(10,10))
        self.TempoGeracao_subTitulo.pack_propagate(False)
        
        self.Valor_TempoGeracao=ctk.CTkLabel(self.TempoDeGeracao,text="0 Horas",font=ctk.CTkFont(size=25,family="Segoe UI",weight="bold"))
        self.Valor_TempoGeracao.pack(anchor="w",padx=(10,0),pady=(8,0))
        self.Valor_TempoGeracao.pack_propagate(False)
        #================================================================
        #Campo de dados do relatorio
        self.CampoDeDadosRelatorio=ctk.CTkFrame(self.aba_Relatorios,fg_color="#E9E9E9",height=100)
        self.CampoDeDadosRelatorio.pack(fill="both",expand=True,padx=10,pady=10)

        self.CampoDeDadosRelatorio_Registros = self.RegistrosInfos("Data", "Energia", "Pico", "Duração")

        self.CampoDeDadosRelatorio_Registros = self.RegistrosInfos("13/10", "5 mW", "6 mW", "2 Horas")

        self.CampoDeDadosRelatorio_Registros = self.RegistrosInfos("12/10", "3 mW", "5 mW", "1 Hora")

        #================================================================
        #Bloco de resumo Operacional e exportação
        self.Bloco_ResumoeExportacao=ctk.CTkFrame(self.aba_Relatorios,fg_color="#E9E9E9",height=180)
        self.Bloco_ResumoeExportacao.pack(fill="both",padx=10,pady=10)
        self.Bloco_ResumoeExportacao.grid_propagate(False)

        self.Bloco_ResumoeExportacao.grid_columnconfigure(0,weight=1)
        self.Bloco_ResumoeExportacao.grid_columnconfigure(1,weight=1)

        self.Resumo_Operacional=ctk.CTkFrame(self.Bloco_ResumoeExportacao,fg_color="#E3E3E3",height=150)
        self.Resumo_Operacional.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
        self.Resumo_Operacional.grid_propagate(False)

        self.Resumo_OperacionalIna=ctk.CTkLabel(self.Resumo_Operacional,text="Dados INA219",font=ctk.CTkFont(size=20,family="Segoe UI",weight="bold"))
        self.Resumo_OperacionalIna.pack()
        self.Resumo_OperacionalIna.pack_propagate(False)

        self.Resumo_OperacionalInaTensao=ctk.CTkLabel(self.Resumo_Operacional,text="Tensão: 0 V",font=ctk.CTkFont(size=15))
        self.Resumo_OperacionalInaTensao.pack(anchor="w",padx=(10,0))

        self.Resumo_OperacionalInaCorrente=ctk.CTkLabel(self.Resumo_Operacional,text="Corrente: 0 A",font=ctk.CTkFont(size=15))
        self.Resumo_OperacionalInaCorrente.pack(anchor="w",padx=(10,0))

        #Exportação
        self.Exportar_Relatorio=ctk.CTkFrame(self.Bloco_ResumoeExportacao,fg_color="#E3E3E3",height=150)
        self.Exportar_Relatorio.grid(row=0,column=1,padx=10,pady=10,sticky="nsew")
        self.Exportar_Relatorio.grid_propagate(False)

    def configuracoes(self):
        pass

#=================================================================================
#=================================Acima front end=================================
#=================================Abaixo Esteticas Extras=========================
#=================================================================================

    def criar_Separador_barra(self):
        self.separador=ctk.CTkFrame(self.Barra_lateral,height=3,corner_radius=0,fg_color="#E3E3E3")
        self.separador.pack(fill="x",padx=12,pady=15)

    def criar_SeparadorAbaCalibracao(self):
        self.Separador_aba=ctk.CTkFrame(self.Calibracao_Motor,height=2,corner_radius=0,fg_color="#D0D0D0")
        self.Separador_aba.pack(fill="x",padx=15,pady=10)

    def criar_SeparadorAbaStatus(self):
            self.Separador_aba=ctk.CTkFrame(self.Status_doSistemaInformacoes,height=2,corner_radius=0,fg_color="#D0D0D0")
            self.Separador_aba.pack(fill="x",padx=15,pady=10)

    def StatusInfos(self,texto_esquerdo,texto_direito):
        self.Espaco=ctk.CTkFrame(self.Status_doSistemaInformacoes,fg_color="transparent")
        self.Espaco.pack(fill="x",padx=20,pady=10)

        self.esquerdo=ctk.CTkLabel(self.Espaco,text=texto_esquerdo,text_color="black",font=ctk.CTkFont(size=16))
        self.esquerdo.pack(side="left")

        self.direito=ctk.CTkLabel(self.Espaco,text=texto_direito,text_color="#777777",font=ctk.CTkFont(size=16))
        self.direito.pack(side="right")

        return texto_direito

    def RegistrosInfos(self,texto_esquerdo,texto_meio_esquerdo,texto_meio_direito,texto_direito):
        self.Espaco=ctk.CTkFrame(self.CampoDeDadosRelatorio,fg_color="transparent")
        self.Espaco.pack(fill="x",padx=20,pady=10)

        for coluna in range(4):
            self.Espaco.grid_columnconfigure(coluna, weight=1)

        self.esquerdo=ctk.CTkLabel(self.Espaco,text=texto_esquerdo,text_color="black",font=ctk.CTkFont(size=16))
        self.esquerdo.grid(row=0,column=0,sticky="w")

        self.meio_esquerdo=ctk.CTkLabel(self.Espaco,text=texto_meio_esquerdo,text_color="#777777",font=ctk.CTkFont(size=16))
        self.meio_esquerdo.grid(row=0,column=1,sticky="w")

        self.meio_direito=ctk.CTkLabel(self.Espaco,text=texto_meio_direito,text_color="#777777",font=ctk.CTkFont(size=16))
        self.meio_direito.grid(row=0,column=2,sticky="w")

        self.texto_direito=ctk.CTkLabel(self.Espaco,text=texto_direito,text_color="#777777",font=ctk.CTkFont(size=16))
        self.texto_direito.grid(row=0,column=3,sticky="w")

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

    def atualizar_graficoPlot(self):
        #Para de atualizar se nao estiver na tela
        if not self.quadro_1Dash.winfo_exists():
            return

        #simula uma leitura de potencia em mW
        PotenciaPlot=round(random.uniform(0, 5), 2)
        horarioPlot= datetime.now()

        #Armazenando os dados obtidos
        self.horariosGraficoPlot.append(horarioPlot)
        self.potenciaGraficoPlot.append(PotenciaPlot)

        #atualiza a linha de grafico
        self.linha_graficoPlot.set_data(list(self.horariosGraficoPlot),list(self.potenciaGraficoPlot))

        #ajustei os eixos
        self.graficoPlot.relim()
        self.graficoPlot.autoscale_view()

        self.canvas_graficoPlot.draw_idle()
        self.quadro_1Dash.after(2000,self.atualizar_graficoPlot)

    def atualizar_graficoFatia(self,angulo):
        # Remove a fatia anterior, caso exista
        if self.fatia_motor is not None:
            self.fatia_motor.remove()

        # Sentido horário
        if angulo >= 0:
            inicio = 90 - angulo
            fim = 90
            cor = "#E2E2E2"

        # Sentido anti-horário
        else:
            inicio = 90
            fim = 90 + abs(angulo)
            cor = "#949494"

        # Criando a fatia colorida
        self.fatia_motor = Wedge(center=(0, 0),r=1,theta1=inicio,theta2=fim,width=0.25,facecolor=cor)

        # Adicionando a fatia ao gráfico
        self.grafico_motorFatia.add_patch(self.fatia_motor)

        # Atualizando o gráfico
        self.canvas_motorFatia.draw_idle()

    def sair_conta(self):
            self.janela_principal.destroy()
            self.construir_login()


janela=aplicativo()
janela.mainloop()