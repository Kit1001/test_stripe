sudo apt install git docker.io -y  
git clone https://github.com/Kit1001/test_stripe.git  
cd test_stripe  
docker build . -t teststripe  
docker run -d -p 80:80 teststripe
