import traceback, json, os
from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel
from rich.padding import Padding

class Test:
    def __init__(self):
        self.showResult = False
        self.console = Console()
        self.tests = 0
        self.cantTest = 0
        self.ClearScreen()
        self.console.print(f"Mostazaniikkk´s Unit test module 🔎⚱️")
        self.console.print("[blink yellow]Remember that errors that appear in white [green underline]are not real errors[/green underline], they are just library tests 🤣[/blink yellow]\n")

    def ErrorPrint(self, var): 
        self.console.print(f"🚨 [bold red]Error[/bold red]: The property {var} does not behave as expected", style="bold red")

    @staticmethod
    def ClearScreen():
        if os.name == 'nt': os.system('cls') # Para Windows
        else: os.system('clear') # Para MacOS y Linux (os.name es 'posix')

    def UnitTest(function):
        def wrapper(self, *args, **kwargs):
            self.cantTest += 1
            try: 
                function(self, *args, **kwargs)
                self.tests += 1
            except Exception as e:
                self.console.print(f"🔥 [bold red u]Critical error[/bold red u]: The last executed module contains a critical error that needs to be urgently patched:", style="bold red")
                traceback_string = traceback.format_exc()
                syntax = Syntax(traceback_string, "python", theme="monokai", line_numbers=False)
                panel = Panel(syntax, width=self.console.width)  # Ajusta el ancho del panel a la mitad del ancho de la consola
                padded_panel = Padding(panel, (1, 2))  # Agrega un margen alrededor del panel
                self.console.print(padded_panel)
        return wrapper
    
    def Exit(self):self.console.print(f"\n{self.tests} out of {self.cantTest} tests passed {'🎉' if self.tests == self.cantTest else '😢'}", style="bold blue")

    def ShowJson(self, value):
        ogJson = json.dumps(value, indent=4)
        syntax = Syntax(ogJson, "json", theme="monokai", line_numbers=True)
        panel = Panel(syntax, width=self.console.width)
        self.console.print(panel, style="bold yellow")

    @UnitTest
    def JsonTest(self, data, result, area, varName):
        dataResult = json.loads(result)

        if area in data and data[area] == dataResult[area]: 
            self.console.print(f"✅ {varName} works correctly.", style="bold green")
            if self.showResult == True: self.ShowJson(data)
        else:
            def ShowData(message, spected, dataResult):
                jsonError = f"{message}:\n\n[green]{dataResult}[/green]\n[red]{spected}[/red]"
                panel = Panel(jsonError, width=self.console.width)
                paddedPanel = Padding(panel, (1,2))
                self.console.print(paddedPanel, style="bold yellow")
            
            self.ErrorPrint(varName)
            ShowData("Original Json", data, result)
            ShowData("Evaluated values comparation", data[area], dataResult[area])

            self.tests -= 1