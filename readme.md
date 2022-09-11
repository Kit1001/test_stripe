
## Запуск
1. Устанавливаем git и docker  
`sudo apt install git docker.io -y`
2. Копируем репозиторий в рабочую директорию  
`git clone https://github.com/Kit1001/test_stripe.git`
3. Переходим в папку проекта  
`cd test_stripe`  
4. Создаем образ из файлов проекта  
`docker build . -t teststripe`  
5. Создаем и запускаем контейнер из полученного образа  
`docker run -d -p 80:80 teststripe`
