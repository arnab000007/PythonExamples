from UIFactory import SupportedPlatforms
from factory import Flutter
from UIElements.Buttons.button import Button

def main():
    flutter = Flutter(SupportedPlatforms.ANDROID)


    uiFactory =  flutter.createUIFactory()

    button: Button = uiFactory.createButton()
    print(button.getinfo())
    uiFactory.createMenu()
    uiFactory.createDropdown()


if __name__ == "__main__":
    main()


