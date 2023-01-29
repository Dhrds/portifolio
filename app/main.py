from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from plyer import email
from kivy.uix.spinner import Spinner

info = {'Local': [], 'Setor': [], 'Tag': [], 'n serie': [], 'vaso em uso': [], 'inst placa de TAG/CAT?': [],
        'Instalar placa indelevel?': [], 'Providenciar 2 saida amplas': [], 'instalar aterramento?': [],
        'Calibrar manometro?': [], 'Calibrar PSV?': [], 'Realizar inspecao ext.?': [], 'Reconstruir Prontuario ?': [],
        'Realizar inspecao int.?': []}
purgador = {'quantidade de purgador':[],'tipo':[],'bitola':[],'joelho':[],
        '1red / ampl macho':[],'red / ampl femea':[],'red / ampl macho':[],
        'conexao t':[],'niple':[],'valvula tripartida':[]}
manometro = {'quantidade de manometro':[],'tipo':[],'bitola':[],'Padrao':[],'seco/glicerinado':[],'intervalo':[],'caixa':[],'joelho':[],
        '1red / ampl macho':[],'red / ampl femea':[],'red / ampl macho':[],
        'conexao t':[],'niple':[],'valvula tripartida':[]}
valvulaSeguranca = {'quantidade de valvula':[],'P.A':[],'Fluido':[],'bitola':[],'joelho':[],
        '1red / ampl macho':[],'red / ampl femea':[],'red / ampl macho':[],
        'conexao t':[],'niple':[],'valvula tripartida':[]}
pressostato = {'quantidade de pressostato':[],'P.A':[],'bitola':[],'joelho':[],
        '1red / ampl macho':[],'red / ampl femea':[],'red / ampl macho':[],
        'conexao t':[],'niple':[],'valvula tripartida':[]}
bloqpsv = {'quantidade de bloqueio PSV':[],'Lacrar bloqueio antes da PSV':[],'bitola':[],'joelho':[],
        '1red / ampl macho':[],'red / ampl femea':[],'red / ampl macho':[],
        'conexao t':[],'niple':[],'valvula tripartida':[]}
bloqmanometro = {'quantidade de bloqueio manometro':[],'Lacrar bloqueio antes do manometro':[],'bitola':[],'joelho':[],
        '1red / ampl macho':[],'red / ampl femea':[],'red / ampl macho':[],
        'conexao t':[],'niple':[],'valvula tripartida':[]}
cliente = (info,purgador,manometro,valvulaSeguranca,pressostato,bloqpsv,bloqmanometro)

class GerenciarTelas(ScreenManager):
    pass

class Menu(Screen):
    pass

class Comp(Screen):
    def finalizar(self):
        info['Local'].append(self.ids.local.text)
        info['Setor'].append(self.ids.setor.text)
        info['Tag'].append(self.ids.insira_tag.text)
        info['n serie'].append(self.ids.nSerie.text)
        info['inst placa de TAG/CAT?'].append(str(list("Sim" if x == True else "Nao" for x in [self.ids.tag_cat.active]
                                                       )).strip('[]').strip("''"))
        info['Instalar placa indelevel?'].append(str(list("Sim" if x == True else "Nao" for x in
                                                          [self.ids.indelevel.active])).strip('[]').strip("''"))
        info['Providenciar 2 saida amplas'].append(str(list("Sim" if x == True else "Nao" for x in
                                                          [self.ids.saida2.active])).strip('[]').strip("''"))
        info['instalar aterramento?'].append(str(list("Sim" if x == True else "Nao" for x in
                         [self.ids.aterramento.active])).strip('[]').strip("''"))
        info['Calibrar manometro?'].append(str(list("Sim" if x == True else "Nao" for x in
                         [self.ids.calibrar_manometro.active])).strip('[]').strip("''"))
        info['Calibrar PSV?'].append(str(list("Sim" if x == True else "Nao" for x in
                         [self.ids.calibrar_psv.active])).strip('[]').strip("''"))
        info['Realizar inspecao ext.?'].append(str(list("Sim" if x == True else "Nao" for x in
                         [self.ids.externa.active])).strip('[]').strip("''"))
        info['Reconstruir Prontuario ?'].append(str(list("Sim" if x == True else "Nao" for x in
                         [self.ids.prontuario.active])).strip('[]').strip("''"))
        info['Realizar inspecao int.?'].append(str(list("Sim" if x == True else "Nao" for x in
                         [self.ids.interna.active])).strip('[]').strip("''"))
        info['vaso em uso'].append(self.ids.vaso.text)       
       
        asd = str(cliente)
        asdf = asd.replace('[','')
        asdf=asdf.replace(']','')
        asdf=asdf.replace(':',',')
        asdf=asdf.replace("'",'')
        asdf=asdf.replace('"','')
        asdf=asdf.replace('{','\n')
        asdf=asdf.replace('}','\n')
        asdf=asdf.replace('(','')
        asdf=asdf.replace(')','')
        asdf=asdf.replace(',',';')
        
        arq = open(r"arq.csv","w").write(asdf)
            
        email.send(recipient='contato@engetap.com.br',
                    subject='app teste',
                    text=asdf,
                    )    

        self.ids.local.text = ""
        self.ids.setor.text = ""
        self.ids.insira_tag.text = ""
        self.ids.nSerie.text = ""
        self.ids.tag_cat.active = False
        self.ids.indelevel.active = False
        self.ids.saida2.active = False
        self.ids.aterramento.active = False
        self.ids.calibrar_manometro.active = False
        self.ids.calibrar_psv.active = False
        self.ids.externa.active = False
        self.ids.prontuario.active = False
        self.ids.interna.active = False
        self.ids.vaso.background_color = (0.0, 0.0, 1.0, 1.0)       

  
    def seguinteNao(self):
        info['Local'].append(self.ids.local.text)
        info['Setor'].append(self.ids.setor.text)
        info['Tag'].append(self.ids.insira_tag.text)
        info['n serie'].append(self.ids.nSerie.text)
        
        self.ids.local.text = ""
        self.ids.setor.text = ""
        self.ids.insira_tag.text = ""
        self.ids.nSerie.text = ""
        
        pass
 
class Tela2(Screen):#Purgador
    def seguinte2(self):
        
        purgador['quantidade de purgador'].append(self.ids.qtpurg.text)
        purgador['tipo'].append(self.ids.purgador0.text)
        
        purgador['bitola'].append(self.ids.purgador1.text)
        purgador['joelho'].append(self.ids.purgador2.text)
        purgador['1red / ampl macho'].append(self.ids.purgador3.text)
        purgador['red / ampl femea'].append(self.ids.purgador4.text)
        purgador['red / ampl macho'].append(self.ids.purgador5.text)
        purgador['conexao t'].append(self.ids.purgador6.text)
        purgador['niple'].append(self.ids.purgador7.text)
        purgador['valvula tripartida'].append(self.ids.purgador8.text)
        

    

    def limpar2(self):
        
        self.ids.purgador0.text = 'tipo'
        self.ids.purgador1.text = 'bitola'
        self.ids.purgador2.text = 'joelho'
        self.ids.purgador3.text = 'red / ampl macho'
        self.ids.purgador4.text = 'red / ampl femea'
        self.ids.purgador5.text = 'red / ampl macho'
        self.ids.purgador6.text = 'conexao t'
        self.ids.purgador7.text = 'niple'
        self.ids.purgador8.text = 'valvula tripartida'

        pass

class Tela3(Screen):#Manometro
    def seguinte3(self):
        
        manometro['quantidade de manometro'].append(self.ids.addman.text)
        manometro['tipo'].append(self.ids.manometro0.text)        
        manometro['bitola'].append(self.ids.manometro1.text)
        manometro['Padrao'].append(self.ids.manometro2.text)
        manometro['seco/glicerinado'].append(self.ids.manometro2.text)
        manometro['intervalo'].append(self.ids.manometro3.text)
        manometro['caixa'].append(self.ids.manometro4.text)
        manometro['seco/glicerinado'].append(self.ids.manometro5.text)
        manometro['1red / ampl macho'].append(self.ids.manometro6.text)
        manometro['red / ampl femea'].append(self.ids.manometro7.text)
        manometro['red / ampl macho'].append(self.ids.manometro8.text)
        manometro['conexao t'].append(self.ids.manometro9.text)
        manometro['niple'].append(self.ids.manometro10.text)
        manometro['valvula tripartida'].append(self.ids.manometro11.text)
   

    def limpar3(self):
        self.ids.addman.text = ''
        self.ids.manometro0.text = 'tipo'
        self.ids.manometro1.text = 'bitola'
        self.ids.manometro2.text = 'Padrao'
        self.ids.manometro5.text = 'seco/glicerinado'
        self.ids.manometro3.text = 'intervalo'
        self.ids.manometro4.text = 'caixa'
        self.ids.manometro5.text = 'seco/glicerinado'
        self.ids.manometro6.text = 'red / ampl macho'
        self.ids.manometro7.text = 'red / ampl femea'
        self.ids.manometro8.text = 'red / ampl macho'
        self.ids.manometro9.text = 'conexao t'
        self.ids.manometro10.text = 'niple'
        self.ids.manometro11.text = 'valvula tripartida'

        
class Tela4(Screen):
    def seguinte4(self):
        
        valvulaSeguranca['quantidade de valvula'].append(self.ids.addvalv.text)
        valvulaSeguranca['P.A'].append(self.ids.valpa.text)        
        valvulaSeguranca['Fluido'].append(self.ids.valfluido.text)
        valvulaSeguranca['bitola'].append(self.ids.valvula0.text)
        valvulaSeguranca['joelho'].append(self.ids.valvula1.text)
        valvulaSeguranca['1red / ampl macho'].append(self.ids.valvula2.text)
        valvulaSeguranca['red / ampl femea'].append(self.ids.valvula3.text)
        valvulaSeguranca['red / ampl macho'].append(self.ids.valvula4.text)
        valvulaSeguranca['conexao t'].append(self.ids.valvula5.text)
        valvulaSeguranca['niple'].append(self.ids.valvula6.text)
        valvulaSeguranca['valvula tripartida'].append(self.ids.valvula7.text)
        pass

    

    def limpar4(self):
        self.ids.addvalv.text = ''
        self.ids.valpa.text = ''
        self.ids.valfluido.text = ''    
        self.ids.valvula0.text = 'bitola'
        self.ids.valvula1.text = 'joelho'
        self.ids.valvula2.text = 'red / ampl macho'
        self.ids.valvula3.text = 'red / ampl femea'
        self.ids.valvula4.text = 'red / ampl macho'
        self.ids.valvula5.text = 'conexao t'
        self.ids.valvula6.text = 'niple'
        self.ids.valvula7.text = 'valvula tripartida'


        pass

class Tela5(Screen):
    def seguinte5(self):
        
        pressostato['quantidade de pressostato'].append(self.ids.addpressos.text)
        pressostato['P.A'].append(self.ids.pressospa.text)        
        pressostato['bitola'].append(self.ids.pressostato0.text)
        pressostato['joelho'].append(self.ids.pressostato1.text)
        pressostato['1red / ampl macho'].append(self.ids.pressostato2.text)
        pressostato['red / ampl femea'].append(self.ids.pressostato3.text)
        pressostato['red / ampl macho'].append(self.ids.pressostato4.text)
        pressostato['conexao t'].append(self.ids.pressostato5.text)
        pressostato['niple'].append(self.ids.pressostato6.text)
        pressostato['valvula tripartida'].append(self.ids.pressostato7.text)

    
    def limpar5(self):
        self.ids.addpressos.text = ''
        self.ids.pressospa.text = ''   
        self.ids.pressostato0.text = 'bitola'
        self.ids.pressostato1.text = 'joelho'
        self.ids.pressostato2.text = 'red / ampl macho'
        self.ids.pressostato3.text = 'red / ampl femea'
        self.ids.pressostato4.text = 'red / ampl macho'
        self.ids.pressostato5.text = 'conexao t'
        self.ids.pressostato6.text = 'niple'
        self.ids.pressostato7.text = 'valvula tripartida'
      
class Tela6(Screen):
    def seguinte6(self):
    
        bloqpsv['quantidade de bloqueio PSV'].append(self.ids.addpsv.text)
        bloqpsv['Lacrar bloqueio antes da PSV'].append(self.ids.psv0.text)        
        bloqpsv['joelho'].append(self.ids.psv1.text)
        bloqpsv['1red / ampl macho'].append(self.ids.psv2.text)
        bloqpsv['red / ampl femea'].append(self.ids.psv3.text)
        bloqpsv['red / ampl macho'].append(self.ids.psv4.text)
        bloqpsv['conexao t'].append(self.ids.psv5.text)
        bloqpsv['niple'].append(self.ids.psv6.text)
        bloqpsv['valvula tripartida'].append(self.ids.psv7.text)
    
    def limpar6(self):
        self.ids.addpsv.text = ''
        self.ids.psv0.text = 'Lacrar bloqueio antes da PSV'   
        self.ids.psv1.text = 'joelho'
        self.ids.psv2.text = 'red / ampl macho'
        self.ids.psv3.text = 'red / ampl femea'
        self.ids.psv4.text = 'red / ampl macho'
        self.ids.psv5.text = 'conexao t'
        self.ids.psv6.text = 'niple'
        self.ids.psv7.text = 'valvula tripartida'
    
class Tela7(Screen):
    def seguinte7(self):
    
        bloqmanometro['quantidade de bloqueio manometro'].append(self.ids.addbloqman.text)
        bloqmanometro['Lacrar bloqueio antes do manometro'].append(self.ids.blocman0.text)        
        bloqmanometro['joelho'].append(self.ids.blocman1.text)
        bloqmanometro['1red / ampl macho'].append(self.ids.blocman2.text)
        bloqmanometro['red / ampl femea'].append(self.ids.blocman3.text)
        bloqmanometro['red / ampl macho'].append(self.ids.blocman4.text)
        bloqmanometro['conexao t'].append(self.ids.blocman5.text)
        bloqmanometro['niple'].append(self.ids.blocman6.text)
        bloqmanometro['valvula tripartida'].append(self.ids.blocman7.text)
        
    def limpar7(self):
        self.ids.addbloqman.text = ''
        self.ids.blocman0.text = 'Lacrar bloqueio'   
        self.ids.blocman1.text = 'joelho'
        self.ids.blocman2.text = 'red / ampl macho'
        self.ids.blocman3.text = 'red / ampl femea'
        self.ids.blocman4.text = 'red / ampl macho'
        self.ids.blocman5.text = 'conexao t'
        self.ids.blocman6.text = 'niple'
        self.ids.blocman7.text = 'valvula tripartida'

class Tela8(Screen):
    def finalizar8(self):
        info['vaso em uso']= self.ids.data_fim.text
        self.ids.data_fim.text = 'data de desativaçao'
        asd = str(cliente)
        asdf = asd.replace('[','')
        asdf=asdf.replace(']','')
        asdf=asdf.replace(':',',')
        asdf=asdf.replace("'",'')
        asdf=asdf.replace('"','')
        asdf=asdf.replace('{','\n')
        asdf=asdf.replace('}','\n')
        asdf=asdf.replace('(','')
        asdf=asdf.replace(')','')
        asdf=asdf.replace(',',';')
        
        arq = open(r"arq1.csv","w")
    
        email.send(recipient='contato@engetap.com.br',
                    subject='app teste',
                    text=asdf,
                    )         
    
class Comparador(MDApp):
    def build(self):

        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.primary_hue = '700'
        return GerenciarTelas()


Comparador().run()
