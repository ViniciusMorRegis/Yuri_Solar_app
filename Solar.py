import customtkinter as ctk
from PIL import Image
import serial

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        

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

#======Acima declaração do front-end
#======Abaixo declaracao do back-end

        #self.verificar_login()

    def construir_login(self):
        self.janela_login=ctk.CTkFrame(self)
        self.janela_login.pack(fill="both",expand=True)

        #==============================================================================================
        #Criando e colocando plano de fundo

        #carregar imagem de fundo
        self.imagem_fundo=ctk.CTkImage(dark_image=Image.open("imagens/planodefundo.png"),size=(self.winfo_screenwidth(),self.winfo_screenheight()))

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
        self.Barra_lateral=ctk.CTkFrame(self.janela_principal,width=200,fg_color="white")
        self.Barra_lateral.pack(side="left",fill="y")

        #============================================================================================
        #Criei um campo para o Norte da barra
        self.Campo_norte_Barra=ctk.CTkFrame(self.Barra_lateral,fg_color="transparent")
        self.Campo_norte_Barra.pack()

        #============================================================================================
        #Criei um campo para o Central da barra
        self.Campo_Central_Barra=ctk.CTkFrame(self.Barra_lateral,fg_color="transparent")
        self.Campo_Central_Barra.pack()

        #============================================================================================
        #Criei um campo para o Sul da barra
        self.Campo_Sul_Barra=ctk.CTkFrame(self.Barra_lateral,fg_color="transparent")
        self.Campo_Sul_Barra.pack()

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

        self.quadro_1=ctk.CTkFrame(self.tela_dashboard)
        self.quadro_1.grid(row=0,column=0,padx=10,pady=10, sticky="nsew")

        self.quadro_2=ctk.CTkFrame(self.tela_dashboard)
        self.quadro_2.grid(row=0,column=1,padx=10,pady=10, sticky="nsew")

        self.quadro_3=ctk.CTkFrame(self.tela_dashboard)
        self.quadro_3.grid(row=1,column=0,padx=10,pady=10, sticky="nsew")

        self.quadro_4=ctk.CTkFrame(self.tela_dashboard)
        self.quadro_4.grid(row=1,column=1,padx=10,pady=10, sticky="nsew")

        #================================================================
        #Inserção dos dados nos seus respectivos quadrantes
        #Quadrante 1
        self.Geracao_Potencia=ctk.CTkLabel(self.quadro_1,text="Geração de Energia (W)",font=ctk.CTkFont(size=50))
        self.valor_Potencia=ctk.CTkLabel(self.quadro_1,text="0.0 W",font=ctk.CTkFont(size=30))

        self.Geracao_Potencia.pack()
        self.valor_Potencia.pack()

        #================================================================
        #Inserção dos dados nos seus respectivos quadrantes
        #Quadrante 2

        self.angulo180=ctk.CTkLabel(self.quadro_2, text="Angulo do Servo: 0°",font=ctk.CTkFont(size=50))
        self.angulo360=ctk.CTkLabel(self.quadro_2, text="Angulo do motor de Passo: 0°",font=ctk.CTkFont(size=30))

        self.angulo180.pack()
        self.angulo360.pack()

        #================================================================
        #Inserção dos dados nos seus respectivos quadrantes
        #Quadrante 3

        self.Luminosidade_Cruz1=ctk.CTkLabel(self.quadro_3,text="Luminosidade do LDR 1:",font=ctk.CTkFont(size=20))
        self.Luminosidade_Cruz2=ctk.CTkLabel(self.quadro_3,text="Luminosidade do LDR 2:",font=ctk.CTkFont(size=20))
        self.Luminosidade_Cruz3=ctk.CTkLabel(self.quadro_3,text="Luminosidade do LDR 3:",font=ctk.CTkFont(size=20))
        self.Luminosidade_Cruz4=ctk.CTkLabel(self.quadro_3,text="Luminosidade do LDR 4:",font=ctk.CTkFont(size=20))

        self.Luminosidade_Cruz1.pack()
        self.Luminosidade_Cruz2.pack()
        self.Luminosidade_Cruz3.pack()
        self.Luminosidade_Cruz4.pack()


    def diagnosticos(self):
        pass

    def relatorios(self):
        pass

    def configuracoes(self):
        pass

#=================================================================================
#=================================Acima front end=================================
#=================================Abaixo backend==================================
#=================================================================================

    def verificar_login(self):
        usuario= self.Campo_nome.get()
        senha= self.Campo_senha.get()

        if usuario == self.usuario_login and senha== self.usuario_senha:
            self.janela_login.destroy()
            self.tela_principal()
        else:
            print("Nome ou senha incorreto")

janela=aplicativo()
janela.mainloop()