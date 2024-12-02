# <img align="left" alt="GitHub" height="30" width="30" src="https://upload.wikimedia.org/wikipedia/commons/3/39/Kubernetes_logo_without_workmark.svg"> Criar Cluster Kubernetes + Deploy de Aplicação Django



## 📌 Objetivo do Projeto:
- Criaremos um Cluster Kubernetes com duas instancias
- Em seguida faremos o deploy da nossa aplicação Django para esse Cluster
- Nossa aplicação é uma página simples de galeria de fotos para exemplificar a implantação de uma aplicação Django em um Cluster Kubernetes utilizando o serviço EKS da AWS.

## 🌐 O que é um Cluster Kubernetes:
- Um cluster Kubernetes é um conjunto de máquinas (físicas ou virtuais) que trabalham juntas para rodar aplicações containerizadas.
- O objetivo é ter uma aplicação com alta disponibilidade garantindo que o sistema esteja sempre disponível, além de distribuir o tráfego de rede de maneira eficiente entre os containers para garantir que a carga seja bem gerenciada e que os recursos não fiquem sobrecarregados.

Vantagens de usar um cluster Kubernetes
1. Gerenciamento de Contêineres.
2. Escalabilidade
3. Alta Disponibilidade
4. Balanceamento de Carga
5. Orquestração de Implantações
6. Infraestrutura como Código
7. Integração com Ecosistemas de DevOps
<br><br>

## 🔧 1 - Criando o Cluster Kubernetes com o serviço EKS da AWS
Certifique-se de que você tem as seguintes ferramentas instaladas no seu computador:

- AWS CLI:  <br>
Siga as instruções oficiais em: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html <br>
Verifique a instalação:
```ShellSession
aws --version
```

- eksctl:  <br>
Instale conforme o sistema operacional:
Linux/macOS
```ShellSession
curl -s --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /usr/local/bin
```
Windows:
```ShellSession
choco install eksctl
```
Verifique:
```ShellSession
eksctl version
```

- kubectl:  <br>
Instale a versão compatível com o Kubernetes:
```ShellSession
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/$(uname -s | tr '[:upper:]' '[:lower:]')/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin
```
Verifique:
```ShellSession
kubectl version --client
```

- Configure a AWS CLI
```ShellSession
aws configure
```
Insira:  <br> Access Key ID  <br> Secret Access Key  <br> Região padrão (ex.: us-east-1)

- Verifique as Permissões da Conta  <br>
Certifique-se de que o usuário tem as permissões adequadas.  <br>
Você pode usar a política gerenciada da AWS chamada AdministratorAccess durante o desenvolvimento.

## <img align="left" alt="GitHub" height="30" width="30" src="https://upload.wikimedia.org/wikipedia/commons/3/39/Kubernetes_logo_without_workmark.svg"> Criar o Cluster EKS:
- Crie o Cluster  <br>
Deve demorar cerca de 15 minutos para a conclusão da criação do Cluster.
```ShellSession
eksctl create cluster \
  --name meu-cluster \
  --region us-east-1 \
  --nodegroup-name meu-grupo-de-nos \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3 \
  --node-type t2.micro \
  --with-oidc \
  --managed
```

A criação pode levar 10 a 15 minutos. Durante o processo, o eksctl cria os seguintes recursos: 
- Cluster EKS.
- Uma VPC com sub-redes.
- Grupos de segurança e outros recursos necessários.
- Nós gerenciados conectados ao cluster.

## 🔨 Configurar o kubectl
- Teste a Conexão
```ShellSession
kubectl get svc
```
Você deve ver o serviço kubernetes listado.

- Verificar o Cluster
```ShellSession
kubectl get nodes
```
O resultado deve mostrar os nós criados no grupo.
Seguindo essas etapas, você terá um cluster Kubernetes funcional na AWS utilizando o serviço EKS e o eksctl.
<br><br>


## 💻 2 - Deploy da Aplicação Django para o Cluster Kubernetes.
- Certifique-se de ter o Docker instalado
```ShellSession
docker --version
```

- Criar a imagem da aplicação
```ShellSession
docker build -t <nome_da_imagem> .  **<nome_da_imagem> deve ser <nome_usuario>/<nome_repositorio>
```

- Subir a imagem para o Docker Hub
```ShellSession
docker login
docker push <nome_da_imagem>
docker logout
```

- Executar o arquivo Kubernetes.yaml 
Acesse a pasta do projeto e execute o comando abaixo
```ShellSession
kubectl apply -f <arquivo_yaml>
```

- Visualizar o Deployment
```ShellSession
kubectl get deployment
```

- Visualizar os Pods
```ShellSession
kubectl get pods
```

- Visualizar o Service
```ShellSession
kubectl get service
```
<br>

## 📡 3 - Acessar a aplicação através do Cluster
Visualize o ip de acesso ao service. É com ele que você acessará a aplicação.
```ShellSession
kubectl get service  <nome_do_service>    **encontra <nome_do_service> com o comando: kubectl get service
```
Acesse pelo navegador:
http:// EXTERNAL-IP
<br><br>

## ⛔ 4 - Destruir o Cluster (Se Necessário)
Utilizar o serviço EKS da AWS implica em custos. <br>
Se você quiser remover o cluster e todos os recursos associados, execute:
```ShellSession
eksctl delete cluster --name meu-cluster --region us-east-1
```
<br>

## 🛠️ Construído com
* [AWS]() - plataforma de serviços de computação em nuvem oferecida pela Amazon
* [EKS]() - serviço gerenciado de Kubernetes da AWS para facilitar a implementação do cluster Kubernetes
* [AWS CLI]() - é uma ferramenta de linha de comando que permite interagir com os serviços da AWS
* [eksctl]() - ferramenta de linha de comando para facilitar a criação, gerenciamento e operação de clusters na Amazon EKS
<br>

## 👨🏼 Autor - Lucas Queiróz
<div align="left"> 
<a  href="https://github.com/lucas-qz" target="_blank"><img align="left" alt="GitHub" height="30" width="30" src="https://img.icons8.com/m_sharp/200/cecece/github.png"> GitHub - Lucas Queiróz </a><br/><br/>
<a  href="https://www.linkedin.com/in/lucas-qz/" target="_blank"><img align="left" alt="Linkedin" height="30" width="30" src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"> Linkedin - Lucas Queiróz </a><br/><br/>
<a  href="http://lucasqz.com.br" target="_blank"><img align="left" alt="Portfólio" height="30" width="30" src="https://cdn-icons-png.flaticon.com/512/5602/5602732.png"> Portfólio - Lucas Queiróz </a><br/><br/>
</div>
<br/><br/>