from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_create_product_form(driver):
    
    driver.get("http://localhost:5173/")
    create_button_product_form_dialog = driver.find_element(By.ID, 'create-button-product-form-dialog')
    create_button_product_form_dialog.click()     

    
    product_form = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "product-form"))
    )   
    assert product_form.is_displayed()   
