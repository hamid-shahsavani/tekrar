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
#### *create loading animation in python cli project ...*<br />
+ ##### Generally you can use tekrar in two methods ...

  + ##### sleep<br />
    ```
    maybe a unique example similar to time.sleep ...
    pause the python cli project and display the loading animation for a few seconds ...
    ```
    
  + ##### function<br />
    ```
    show loading animation will be displayed until the function process is completed ...
    ```



---
## *installation*

+ #### *install by pip*

      # linux
      
      sudo python3 -m pip install tekrar
      
      # windows
      
      py -m pip install tekrar
      
+ #### *install by setup.py*

      # linux
      
      sudo python3 -m pip install https://github.com/sys113/tekrar/archive/0.1.1.zip
      
      # windows
      
      py -m pip install https://github.com/sys113/tekrar/archive/0.1.1.zip

---
## *example*
  
  + #### *function*
  
    + [1 : curl download file](https://raw.githubusercontent.com/sys113/tekrar/master/example/function_example_one.gif)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```arguments used : function, argument, speed, output```
    + [2 : write numbers 1 to 333333 in a file](https://raw.githubusercontent.com/sys113/tekrar/master/example/function_example_two.gif)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```arguments used : function, speed, method, output and save function return value```
    
   + #### *sleep*
   
   + [1 : show loading animation for a few seconds](https://raw.githubusercontent.com/sys113/tekrar/master/example/sleep_example_one.gif)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```arguments used : sleep , speed , method```
  
---
## *description*
  + #### *speed*
    ```python
      # set loading speed ...
      
      # range 1 to 10 ...
      # default value is 3 ...
      
      speed = 5
    ```
    
  + #### *method*
    ```python
      # set loading animation method ...
      
      # only 1 or 2 ...
      # default value is 1 ...
      
      method = 2
    ```
      - #### *method 1*
      
      <div align="center">
      <img src="https://raw.githubusercontent.com/sys113/tekrar/master/example/review%20loading%20animation%20-%20method%20one.gif" width="300" height="40" />
      </div>
      
      - #### *method 2*
      
      <div align="center">
      <img src="https://raw.githubusercontent.com/sys113/tekrar/master/example/review%20loading%20animation%20-%20method%20two.gif" width="300" height="40" />
      </div>

  + #### *sleep*
    ```python
    
      # pause the python cli project and display the loading animation for 8 seconds ...
      # maybe a unique example similar to time.sleep ...
      
      # argument 'sleep' must be a int type ...
      # cannot use simultaneously 'sleep' and 'function' argument ...
      
      sleep = 8
    ```
    
  + #### *function*
    ```python
      # show loading if 'x' function running ...
      
      # cannot use simultaneously 'sleep' and 'function' argument ...
      
      function = x
    ```
    
   + #### *argument*
     ```python
     # use this method if 'function' has 'argument' ...

     # argument 'argument' must be a int type ...

     argument = ['tekrar','SYS113']
     ```
   
   + #### output
     ```python
     # if 'function' has arguments then use this way for hide function output ...

     # default value is True
     # argument 'output' must be boolean type ...

     output = True
     ```
     
   + #### save function return value
      ```python
      # call tekrar.loading function in a variable ...

      save_return_value = tekrar.loading(function = func, argument = ['hi'], output = True, speed = 5, method = 2)
      ```
   
---
## *copyright*
*copyright <ins>SYS113</ins> - <ins>2019</ins>.*

---
## *license* 
*<ins>MIT</ins> license , please see <ins>LICENSE</ins> file.*

---
## *donate* 
+ *for <ins>iranian</ins> users &nbsp; :  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <ins>  id pay </ins> &nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://idpay.ir/sys113*
+ *for <ins>global</ins> users &nbsp; : &nbsp;<ins>BTC wallet id</ins>&nbsp; - &nbsp; 149JgUmFqG6MvFg79Ldrvdk2bN35ByhMuw*
---
## *contact me* 
* *[email](mailto:051.SYS113@gmail.com)*
* *[telegram](https://t.me/SYS113/)*
* *[instagram](https://instagram.com/sys113/)*
---
## *last world*
*hope this is <ins>tekrar</ins> useful to you and enjoy it.*

---
<div align="center">

*tekrar logo ❤️ mohamad moradiyani*
</div>

---

