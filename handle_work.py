# -*- coding: utf-8 -*-
#  filename: handle_work.py
import hashlib
import reply
import receive
import web

class Handle(object):

    def GET(self):
        try:
            data = web.input()
            print data
        except Exception, e:
            raise
        else:
            pass
        finally:
            pass

'''
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "hello2018"  # 请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print
            "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument
'''
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