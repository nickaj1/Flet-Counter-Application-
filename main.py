import flet as ft 
from flet import TextField
from flet_core.control_event import ControlEvent


def main(page: ft.Page) -> None:
    ''' The Main funtion of the app 
         Displays the page, holds the buttons 
         and handles all the functionality'''
    
    page.title = 'Increment counter'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # Center the element

    # Without this the theme mode is set to the default theme mode of your computer
    page.theme_mode = 'light'  # Set the theme mode to light

    text_number: TextField = TextField(value='0', text_align=ft.TextAlign.CENTER, width=100) # This display the text box where the text is shown


# Functionality of the button of the app for both increment and decrement
    def decrement(e: ControlEvent) -> None:
        '''Decrement a value by 1'''
        text_number.value = str(int(text_number.value) - 1) # Convert the value to an int before the number is subtracted and after it convert back to a string, since the text field holds a string
        page.update()

    
    def increment(e: ControlEvent) -> None:
        '''Increment a value by 1'''
        text_number.value = str(int(text_number.value) + 1)  # Convert the value to an int before the number is add and after it convert back to a string, since the text field holds a string
        page.update()

    

    page.add(
        ft.Row(
           [ft.IconButton(ft.icons.REMOVE, on_click=decrement),
             text_number,
             ft.IconButton(ft.icons.ADD, on_click=increment)],
             alignment = ft.MainAxisAlignment.CENTER # This align everything of the center of the program
        )
    )

if __name__ == '__main__':
    '''This run the app but also the view=ft.AppView.WEB_BROWSER
    runs the app in web mode'''
    ft.app(target=main)    

# veiw=ft.AppView.WEB_BROWSER
