# coding: UTF-8
from __future__ import print_function

import boto3,os
import json,logging,re
import http.client, urllib.parse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('Loading function')

def lambda_handler(event, context):
    
    # このサービスが動作するか決定する。動作条件は、「私は誰」という単語が含まれているかどうか。
    lineText = event["lineMessage"]["events"][0]["message"]["text"]
    logger.info(lineText)
    if "私は誰" not in lineText :
        logger.info("応答すべきメッセージではない")
        return 
    
    # メッセージタイプがUserではない場合は応答しない
    if "user" !=  event["lineMessage"]["events"][0]["source"]["type"] :
        logger.info("メッセージタイプがUserではない")
        return 
        
    # 応答メッセージ組み立て
    repMessage = "uesrId=" +  event["lineMessage"]["events"][0]["source"]["userId"] 
    #repMessage += "replyToken=" +  event["lineMessage"]["events"][0]["replyToken"]
    
    logger.info(repMessage)

    # メッセージを送信したUserのIDを返す
    return {
         "message" : repMessage
    }
    
