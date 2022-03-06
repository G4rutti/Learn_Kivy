from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #Iniciar infinitas palavras chaves
    def __init__(self, **kwargs):
        #Chamar o construtor grid layout
        super(MyGridLayout, self).__init__(**kwargs)

        #set columns
        self.cols = 1

        #Create a second gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        #add widgets
        self.top_grid.add_widget(Label(text='Nome: '))
        #add input box
        self.nome = TextInput(multiline=False)
        self.top_grid.add_widget(self.nome)
        
        #add widgets
        self.top_grid.add_widget(Label(text='Pizza favorita: '))
        #add input box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        #add widgets
        self.top_grid.add_widget(Label(text='Time do Coração: '))
        #add input box
        self.time = TextInput(multiline=False)
        self.top_grid.add_widget(self.time)

        #add the top_grid to the layout
        self.add_widget(self.top_grid)

        

        #Criar o Botão
        self.enviar = Button(text='Enviar', font_size = 32)
        #Bind(ligar) the button
        self.enviar.bind(on_press=self.press_func)
        self.add_widget(self.enviar)

    def press_func(self, instance):
        name = self.nome.text
        pizza = self.pizza.text
        club = self.time.text

        self.add_widget(Label(text=f'Olá, {name}! Você torce para o(a) {club} e gosta da pizza de {pizza}'))
        
        #Clear the input boxes
        self.nome.text = ''
        self.pizza.text = ''
        self.time.text = ''

class MyAppApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyAppApp().run()