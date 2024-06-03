# Projet-CODEVSI-Mangeoire-connectee
IMT Atlantique est refuge LPO (Ligue pour la Protection des Oiseaux), ce qui l’engage notamment à préserver la
biodiversité et à faciliter la nidification des oiseaux, notamment des mésanges. Pour sensibiliser davantage les
étudiants et le personnel de Brest à la biodiversité, il est proposé de fabriquer une mangeoire connectée,
permettant le visionnage des images depuis l’intranet d’IMT Atlantique. Un projet antérieur mené dans le
cadre du CODEVSI ayant défriché et analysé de premières solutions, nous allons reprendre le travail effectué et
explorer de nouvelles directions.

L’objectif de ce projet est donc de réaliser une mangeoire connectée en utilisant le matériel disponible au
FabLab de l’école, équipée d’un distributeur automatique de graine ainsi que d’une caméra permettant le
visionnage d’un flux vidéo sur l’intranet.

Dans le cadre de ce projet, nous utilisons une carte Raspberry Pi 3b+, ainsi que les bibliothèques suivantes :
- Numpy
- Tensorflow
- RPi.GPIO
- Libcamera
- Picamera2


Pour récupérer l'adresse IP de la carte raspberry, on utilise la commande suivante dans un terminal : hostname -I
Pour récupérer les fichier en local, il faut utiliser la commande suivante :
scp -r mangeoire@<adresse_IP_de_la_Raspberry_Pi>:/home/mangeoire/Documents/programmes/Photo <chemin_de_destination_local>
Le mot de passe est alors demandé. Il suffit de le rentrer dans le terminal pour activer le transfert

