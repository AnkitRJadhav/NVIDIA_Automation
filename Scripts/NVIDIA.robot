*** Settings ***
Resource   ../Keywords/NVIDIA_Keywords.robot
Library   SeleniumLibrary
*** Test Cases ***
Validate_NVIDIA_Official_Site
    Open_And_Validate_Product_Tab
    Open_And_Validate_Solution_Tab

