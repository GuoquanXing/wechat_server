# -*- coding: utf-8 -*-
#  python version: 2.7.x, python 3.x is not supported
#  filename: handle_work.py
import hashlib
import reply
import receive
import web
from WXBizMsgCrypt import WXBizMsgCrypt
import messageBrokerConf

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
            print 'URL paramter received:', [signature, timestamp, nonce, echostr]

            wxcpt=WXBizMsgCrypt(messageBrokerConf.Token, messageBrokerConf.EncodingAESToken, messageBrokerConf.CorporateID)
            ret,sEchoStr=wxcpt.VerifyURL(signature, timestamp,nonce,echostr)
            print 'Decoded String:', sEchoStr
            print 'return code:', ret
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
