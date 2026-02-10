from selenium.webdriver.common.by import By

class QuestionSection:
    def __init__(self, component_id):
        self.component_id = component_id

    @property
    def heading(self):
        return (By.ID, f'accordion__heading-{self.component_id}')
    
    @property
    def panel(self):
        return (By.ID, f'accordion__panel-{self.component_id}')

