# Command Line For The Win

The .png and .jpg files (image files) were added to the sandbox by the use of the sftp command-line tool. Below are the steps I used in adding these image files to my sandbox before pushing thge update to githb:

first I moved into the directory where the files I want to upload are located

```bash
cd path/to/my/image/files
```
then:

```bash
sftp <my_sandbox_username>@<my_sandbox_localhost>
```
this line of command triggers a prompt for me to inpt my password for authentication

after the authentication, I was brought to a new interface, of course the sftp interface!

now in the sftp interface (which is shell-like in nature):

```bash
put 0-first_9_tasks.png .
```
```bash
put 0-first_9_tasks.jpg .
```
```bash
put 1-next_9_tasks.png .
```
```bash
put 1-next_9_tasks.jpg .
```
```bash
put 2-next_9_tasks.png .
```
```bash
put 2-next_9_tasks.jpg .
```

And viola, everything gets uploaded!

How was this tutorial, did you enjoy it? 
I know you love my tutorial but you woudn't admit it.
That's alright, programmers are meant to be like that! :)

Hey, don't be heartless, okay. Promise you won't score me bad :)

Love ya!
