from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_agregar_producto_carrito():
    driver = webdriver.Chrome()
    try: 
        # 1. login 
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()
    
        assert "/inventory.html" in driver.current_url

        # 2. Agregar producto al carrito
        boton_agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        nombre_producto_inventario = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
        boton_agregar.click()

        