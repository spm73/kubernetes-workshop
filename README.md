# 🎓 Taller introductorio a Kubernetes

¡Hola! En este taller vamos a realizar el despliegue de un proyecto muy básico de aula inteligente basada en Home Assistant (HA) empleando Kubernetes.

Aprenderemos a crear un clúster de Kubernetes usando `microk8s` en varias máquinas virtuales que pueden estar en ordenadores distintos, crearemos **Deployments** para lanzar nuestros contenedores, utilizaremos **volumenes** para almacenar datos y usaremos **servicios** para poder acceder a nuestro aula inteligente.

---

## 📚 Material de apoyo
A continuación, os adjuntamos una serie de recursos para poder consultar los conceptos teóricos que vamos a gastar en el taller:

* **[📽️ Presentación del taller]():** — *Aquí encontrarás un resumen de los conceptos clave.*
* **[📖 Documentación (Wiki)](https://marcelosaval.github.io/Wiki-IMCR/Cloud%20Computing/KubernetesYCloudComputing/):** — *Entrada de la wiki de la asignatura de IMCR donde se expone más detalladamente cada concepto.*

---

## 🛠️ Requisitos Previos
* **VirtualBox** instalado en tu ordenador.
* Descargar el archivo de la máquina virtual. (`kubernetes-base.ova`). *Este archivo es una imagen de Ubuntu 24.04 LTS con `microk8s` instalado y con un servidor NFS configurado*.

---

## 🚀 Fase 1: Importar la Infraestructura

1. Abre VirtualBox.
2. Ve a **Archivo > Importar servicio virtualizado**.
3. Selecciona el archivo `kubernetes-base.ova` que has descargado.
4. ⚠️ **¡Paso Crítico!** En la ventana de configuración, busca el desplegable **"Política de direcciones MAC"** y asegúrate de seleccionar: **"Generar nuevas direcciones MAC para todos los adaptadores de red"**. *(Si no haces esto, chocarás con la IP de tus compañeros).*
5. Haz clic en **Terminar** y espera a que se complete la importación.
6. Arranca la máquina virtual. La contraseña para el usuario `user` es `user1234`.

---