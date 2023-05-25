#!/bin/bash
# $1: 用户名  $2: 仓库 $3: github token
curl -X POST https://api.github.com/repos/$1/$2/dispatches \
    -H "Accept: application/vnd.github.everest-preview+json" \
    -H "Authorization: token $3" \
    --data '{"event_type": "每日图片更新"}'
