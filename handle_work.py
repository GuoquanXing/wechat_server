# -*- coding: utf-8 -*-
#  filename: handle_work.py
import hashlib
import reply
import receive
import web
from WXBizMsgCrypt import WXBizMsgCrypt

class Handle(object):

    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "no paramter given"    
            print data
            signature = data.msg_signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr

            token = "hello2018"  # 请按照公众平台官网\基本配置中信息填写
            encodingAESToken = 'Fc72tGGPgLdJHThLJsTNtFa5KgpVL8WFIuR7K2Xd61r'
            corporateID = 'ww4cf07f7d23045699'
            
            wxcpt=WXBizMsgCrypt(token, encodingAESToken, corporateID)
            print [signature, timestamp, nonce, echostr]
            ret,sEchoStr=wxcpt.VerifyURL(signature, timestamp,nonce,echostr)
            print sEchoStr
            print 'return code:' ret
            return sEchoStr

        except Exception, e:
            raise
        else:
            pass
        finally:
            pass

    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData    #后台打日志
            
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):

                if recMsg.MsgType == 'text':
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    content = "You told me:" + recMsg.Content + ",thanks!"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()

                if recMsg.MsgType == 'image':
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()

            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment
