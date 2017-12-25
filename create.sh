#!/bin/bash
# This is script of the generation video from "Gource".

# project: Screensaver Kodi Universe (http://berserk.tv)
# This script creates a ZIP archive of a Kodi screensaver.
# GNU GENERAL PUBLIC LICENSE. Version 2, June 1991
# 
# скрипт запускается под обычным пользователем,
# но вначале своего выполнения требует установки пакетов 
# git zip ffmpeg gource с помощью команды sudo

OUT_DIR="output"
OUT="kodi-universe.mkv"
NAME_PROJ="screensaver.kodi.universe"
MEDIA_PATH="${NAME_PROJ}/resources/skins/default/media"
NAME_REP="https://github.com/berserktv/${NAME_PROJ}.git"

GSFILE="output.ppm"
SECONDS_PER_DAY="1"
GOURCE_FRAME_RATE="30"
RESOLUTION="-1920x1080"
CODEC_OUT_FRAME_RATE="25"

# -vcodec  -  кодек для кодирования видеопотока, libx264 в настоящий момент наиболее современный и быстрый кодек (h.264)
# -profile -  профиль для кодека (baseline, main, high, high10, high422, high444)
# -pix_fmt -  установка пиксельного формата (yuv420p, yuv422p, yuv444p)
FFPARAM="-vcodec libx264 -profile:v high422 -pix_fmt yuv420p"
GSPARAM1="--camera-mode track ${RESOLUTION} --stop-position 1.0 --seconds-per-day ${SECONDS_PER_DAY}"
GSPARAM2="--git-branch origin/master --multi-sampling --stop-at-end --hide-filenames"
GSPARAM3="--highlight-users --file-idle-time 13 --max-files 0 --hide date"
GSPARAM4="--title Kodi --bloom-multiplier 1.0 --bloom-intensity 1.0"

VIS="visualize"
# GIT адрес проекта по которому будем создавать визуализацию работы
GIT_REP="https://github.com/xbmc/xbmc.git"
# arg1 - визуализация любого git проекта, который можно задать первым аргументом в командной строке
# example: ./create.sh "https://github.com/facebook/react.git"
if [ -n "$1" ]; then GIT_REP="$1"; fi

# установка пакетов git zip ffmpeg и gource
packages="git zip ffmpeg gource"
for i in $packages; do
  if ! dpkg -s $i | grep -q "install ok installed"; then sudo apt-get install -y $i; fi
done 

# очистка выходного каталога
test -d ${OUT_DIR} && rm -rf ${OUT_DIR}
test -d ${OUT_DIR} || mkdir -p ${OUT_DIR}

cd ${OUT_DIR}
# загружаю Screensaver Kodi Universe и GIT проект, для визуализации 
if ! git clone ${NAME_REP} ${NAME_PROJ}; then echo "Error, not load ${NAME_REP}, exit ..."; exit 1; fi
if ! git clone ${GIT_REP} ${VIS};        then echo "Error, not load ${GIT_REP},  exit ..."; exit 2; fi


# генерация видео для screensaver Kodi Universe - "Вселенная Коди"
gource ${VIS} ${GSPARAM1} ${GSPARAM2} ${GSPARAM3} ${GSPARAM4} --output-framerate ${GOURCE_FRAME_RATE} --output-ppm-stream ${GSFILE}
ffmpeg -y -r ${GOURCE_FRAME_RATE} -f image2pipe -vcodec ppm -i ${GSFILE} ${FFPARAM} -r ${CODEC_OUT_FRAME_RATE} ${OUT} && sync
mv -f ${OUT} ${MEDIA_PATH}
rm -f ${GSFILE}

# секция работы с архивом
# удаляю служебную GIT информацию из проекта screensaver.kodi.universe
test -d ${NAME_PROJ}/.git &&  rm -fr ${NAME_PROJ}/.git
zip -r ${NAME_PROJ}.zip ${NAME_PROJ}

