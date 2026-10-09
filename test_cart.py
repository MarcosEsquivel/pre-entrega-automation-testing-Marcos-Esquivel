import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_agregar_producto_al_carrito():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")

        boton_login.click()
