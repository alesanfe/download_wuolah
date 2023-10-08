# Importa la biblioteca necesaria
from time import sleep

class BrowserAutomation:
    def __init__(self):
        self.open_browser()

    def open_browser(self):
        type("t", KEY_WIN)
        click("chrome.png")
        wait(3)
        click("guess_mode.png")
        wait(3)

    def open_temp_mail(self):
        self.open_url("https://temp-mail.org/es/")
        self.wait_for_element("delete_mode.png")
        click("delete_mode.png")
        wait(15)
        click("copy_email.png")
        click("create_new_page.png")

    def open_url(self, url):
        type(url)
        type(Key.ENTER)

    def register_wuolah(self):
        self.open_url("https://wuolah.com/")
        wait(15)
        click("accept_cookies.png")
        wait(3)
        click("register_wuolah.png")
        self.wait_for_element("open_more_options.png")
        click("open_more_options.png")
        self.select_email()
        type("N3v3r_G0nn@_G1v3_Y0u_Up!")
        self.wait_for_element("create_new_account.png")
        click("create_new_account.png")

    def select_email(self):
        self.wait_for_element("select_email.png")
        click(Pattern("select_email.png").targetOffset(-13,122))
        wait(3)
        type("v", KeyModifier.CTRL)
        click("select_password_input.png")

    def select_university(self):
        wait(3)
        click("spain.png")
        self.wait_for_element("university.png")
        click("university.png")
        type("Sevilla")
        self.wait_for_element("seville_university.png")
        click("seville_university.png")
        type("Inform")
        click("software_engineer.png")
        self.wait_for_element("continue.png")
        click("continue.png")

    def open_email_page(self):
        self.open_url("https://correo.temporal.com/")

    def scroll_down_email(self):
        while not exists(Pattern("notification.png").targetOffset(2,-11)):
            click("down.png")
        click(Pattern("notification.png").targetOffset(6,-11))

    def confirm_email(self):
        self.scroll_down_email()
        self.wait_for_element("confirm.png")
        click("confirm.png")

    def download_files_repeatedly(self):
        while True:
            self.wait_for_element("download.png")
            click("download.png")
            self.wait_for_element("options_download.png")
            click(Pattern("options_download.png").targetOffset(142,-60))
            self.wait_for_element("exit_file.png")
            while not exists(Pattern("exit_file.png").targetOffset(753,-6)):
                if exists(Pattern("not_a_robot.png").targetOffset(-158,-6)):
                    click(Pattern("not_a_robot.png").targetOffset(-158,-3))
                sleep(5)
            click(Pattern("exit_file.png").targetOffset(753,-6))

    def wait_for_element(self, image, timeout=10):
        for _ in range(timeout):
            if exists(image):
                return True
            sleep(1)
        return False

if __name__ == "__main__":
    automation = BrowserAutomation()
    automation.open_temp_mail()
    automation.register_wuolah()
    automation.select_university()
    automation.open_email_page()
    automation.confirm_email()
    automation.download_files_repeatedly()

    





       
