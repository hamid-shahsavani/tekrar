<p align="center">
  <img width="350" height="350" src="https://raw.githubusercontent.com/sys113/tekrar/master/tekrar.png">
</p>

---
<div align="center">
  
![](https://img.shields.io/github/stars/SYS113/tekrar.svg)
![](https://img.shields.io/badge/language-python-orange.svg)
![](https://img.shields.io/github/forks/SYS113/tekrar.svg)
![](https://img.shields.io/github/release/SYS113/tekrar.svg)
![](https://img.shields.io/github/issues/SYS113/tekrar.svg)
![](https://img.shields.io/badge/license-MIT-informational.svg)
</div>

---
## *what is <ins>tekrar</ins>*
*create loading animation in python cli project ...<br />*

---
## *installation*

+ #### *install by pip*

      # linux
      
      sudo python3 -m pip install tekrar
      
      # windows
      
      py -m pip install tekrar
      
+ #### *install by setup.py*

      # linux
      
      sudo python3 -m pip install https://github.com/sys113/tekrar/archive/0.1.0.zip
      
      # windows
      
      py -m pip install https://github.com/sys113/tekrar/archive/0.1.0.zip

---
## *description*
  + #### *speed*
    ```python
      # set loading speed ...
      # range 1 to 10 ...
      
      speed = 5
    ```
    
  + #### *method*
    ```python
      # set loading method ...
      # only 1 or 2 ...
      # default is 1 ...
      
      method = 2
    ```
      - #### *method 1*
      
      <div align="center">
  
      ![Alt Text](https://raw.githubusercontent.com/sys113/tekrar/master/example/review%20loading%20animation%20-%20method%20one.gif)
      </div>
      
      - #### *method 2*
      
      <div align="center">
  
      ![Alt Text](https://raw.githubusercontent.com/sys113/tekrar/master/example/review%20loading%20animation%20-%20method%20two.gif)
      </div>

  + #### *sleep*
    ```python
      # Show loading for 8 second ...
      # can be of type int or float ...
      # cannot use simultaneously 'sleep' and 'function' argument ...
      
      sleep = 8
    ```
    
  + #### *function*
    ```python
      # Show loading if 'x' function running ...
      # cannot use simultaneously 'sleep' and 'function' argument ...
      
      function = x
    ```
    
   + #### *args*
   ```python
   # if function has arguments then use this way ...
   # type 'args' only list ...
   
   args = ['tekrar','SYS113']
