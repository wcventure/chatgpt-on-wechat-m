# encoding:utf-8

from bot.bot import Bot
from bot.chatgpt.chat_gpt_session import ChatGPTSession
from bot.openai.open_ai_image import OpenAIImage
from bot.session_manager import Session, SessionManager
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from config import conf, load_config, load_config_wcventure
from common.log import logger
from common.token_bucket import TokenBucket
from common.expired_dict import ExpiredDict
import openai
import openai.error
import time

# OpenAI对话模型API (可用)
class ChatGPTBot(Bot,OpenAIImage):
    def __init__(self):
        super().__init__()
        # set the default api_key
        openai.api_key = conf().get('open_ai_api_key')
        if conf().get('open_ai_api_base'):
            openai.api_base = conf().get('open_ai_api_base')
        proxy = conf().get('proxy')
        if proxy:
            openai.proxy = proxy
        if conf().get('rate_limit_chatgpt'):
            self.tb4chatgpt = TokenBucket(conf().get('rate_limit_chatgpt', 20))
        
        self.sessions = SessionManager(ChatGPTSession, model= conf().get("model") or "gpt-3.5-turbo")

    def reply(self, query, context=None):
        # acquire reply content
        if context.type == ContextType.TEXT:
            logger.info("[CHATGPT] query={}".format(query))


            session_id = context['session_id']
            reply = None
            clear_memory_commands = conf().get('clear_memory_commands', ['#清除记忆'])
            if query in clear_memory_commands:
                self.sessions.clear_session(session_id)
                reply = Reply(ReplyType.INFO, '记忆已清除')
            elif query == '#清除所有':
                self.sessions.clear_all_session()
                reply = Reply(ReplyType.INFO, '所有人记忆已清除')
            elif query == '#更新配置':
                load_config()
                reply = Reply(ReplyType.INFO, '配置已更新')
            elif query == '清除记忆':
                self.sessions.clear_session(session_id)
                reply = Reply(ReplyType.INFO, '记忆已清除')
            elif query == '清除所有':
                self.sessions.clear_all_session()
                reply = Reply(ReplyType.INFO, '所有人记忆已清除')
            elif query == '更新配置':
                load_config()
                reply = Reply(ReplyType.INFO, '配置已更新')
            elif query == '专业模式1':
                mgs = load_config_wcventure("1")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "1")
                reply = Reply(ReplyType.INFO, '已进入专业模式1\n' + mgs)
            elif query == '专业模式2':
                mgs = load_config_wcventure("2")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "2")
                reply = Reply(ReplyType.INFO, '已进入专业模式2\n' + mgs)
            elif query == '专业模式3':
                mgs = load_config_wcventure("3")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "3")
                reply = Reply(ReplyType.INFO, '已进入专业模式3\n' + mgs)
            elif query == '专业模式4':
                mgs = load_config_wcventure("4")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "4")
                reply = Reply(ReplyType.INFO, '已进入专业模式4\n' + mgs)
            elif query == '专业模式5':
                mgs = load_config_wcventure("5")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "5")
                reply = Reply(ReplyType.INFO, '已进入专业模式5\n' + mgs)
            elif query == '专业模式6':
                mgs = load_config_wcventure("6")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "6")
                reply = Reply(ReplyType.INFO, '已进入专业模式6\n' + mgs)
            elif query == '专业模式7':
                mgs = load_config_wcventure("7")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "7")
                reply = Reply(ReplyType.INFO, '已进入专业模式7\n' + mgs)
            elif query == '专业模式8':
                mgs = load_config_wcventure("8")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "8")
                reply = Reply(ReplyType.INFO, '已进入专业模式8\n' + mgs)
            elif query == '专业模式9':
                mgs = load_config_wcventure("9")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "9")
                reply = Reply(ReplyType.INFO, '已进入专业模式9\n' + mgs)
            elif query == '专业模式10':
                mgs = load_config_wcventure("10")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "10")
                reply = Reply(ReplyType.INFO, '已进入专业模式10\n' + mgs)
            elif query == '专业模式11':
                mgs = load_config_wcventure("11")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "11")
                reply = Reply(ReplyType.INFO, '已进入专业模式11\n' + mgs)
            elif query == '专业模式12':
                mgs = load_config_wcventure("12")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "12")
                reply = Reply(ReplyType.INFO, '已进入专业模式12\n' + mgs)
            elif query == '专业模式13':
                mgs = load_config_wcventure("13")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "13")
                reply = Reply(ReplyType.INFO, '已进入专业模式13\n' + mgs)
            elif query == '专业模式14':
                mgs = load_config_wcventure("14")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "14")
                reply = Reply(ReplyType.INFO, '已进入专业模式14\n' + mgs)
            elif query == '专业模式15':
                mgs = load_config_wcventure("15")
                self.sessions.clear_session(session_id)
                session = self.sessions.session_query_wcventure(query, session_id, "15")
                reply = Reply(ReplyType.INFO, '已进入专业模式15\n' + "You should give me the input in the following form:\n###Function: <<<func1, func2>>>\n\n###CODE: <<<\n...\n>>>")
            elif query == '功能说明' or query == '功能介绍' or query == '专业模式':
                mgs = load_config_wcventure("0")
                reply = Reply(ReplyType.INFO, '功能说明：\n' + mgs)

            if reply:
                return reply
            session = self.sessions.session_query(query, session_id)
            logger.debug("[CHATGPT] session query={}".format(session.messages))

            api_key = context.get('openai_api_key')

            # if context.get('stream'):
            #     # reply in stream
            #     return self.reply_text_stream(query, new_query, session_id)

            reply_content = self.reply_text(session, session_id, api_key, 0)
            logger.debug("[CHATGPT] new_query={}, session_id={}, reply_cont={}, completion_tokens={}".format(session.messages, session_id, reply_content["content"], reply_content["completion_tokens"]))
            if reply_content['completion_tokens'] == 0 and len(reply_content['content']) > 0:
                reply = Reply(ReplyType.ERROR, reply_content['content'])
            elif reply_content["completion_tokens"] > 0:
                self.sessions.session_reply(reply_content["content"], session_id, reply_content["total_tokens"])
                reply = Reply(ReplyType.TEXT, reply_content["content"])
            else:
                reply = Reply(ReplyType.ERROR, reply_content['content'])
                logger.debug("[CHATGPT] reply {} used 0 tokens.".format(reply_content))
            return reply

        elif context.type == ContextType.IMAGE_CREATE:
            ok, retstring = self.create_img(query, 0)
            reply = None
            if ok:
                reply = Reply(ReplyType.IMAGE_URL, retstring)
            else:
                reply = Reply(ReplyType.ERROR, retstring)
            return reply
        else:
            reply = Reply(ReplyType.ERROR, 'Bot不支持处理{}类型的消息'.format(context.type))
            return reply

    def compose_args(self):
        return {
            "model": conf().get("model") or "gpt-3.5-turbo",  # 对话模型的名称
            "temperature":conf().get('temperature', 0.9),  # 值在[0,1]之间，越大表示回复越具有不确定性
            # "max_tokens":4096,  # 回复最大的字符数
            "top_p":1,
            "frequency_penalty":conf().get('frequency_penalty', 0.0),  # [-2,2]之间，该值越大则更倾向于产生不同的内容
            "presence_penalty":conf().get('presence_penalty', 0.0),  # [-2,2]之间，该值越大则更倾向于产生不同的内容
            "request_timeout": conf().get('request_timeout', 60),  # 请求超时时间，openai接口默认设置为600，对于难问题一般需要较长时间
            "timeout": conf().get('request_timeout', 120), #重试超时时间，在这个时间内，将会自动重试
        }

    def reply_text(self, session:ChatGPTSession, session_id, api_key, retry_count=0) -> dict:
        '''
        call openai's ChatCompletion to get the answer
        :param session: a conversation session
        :param session_id: session id
        :param retry_count: retry count
        :return: {}
        '''
        try:
            if conf().get('rate_limit_chatgpt') and not self.tb4chatgpt.get_token():
                raise openai.error.RateLimitError("RateLimitError: rate limit exceeded")
            # if api_key == None, the default openai.api_key will be used
            response = openai.ChatCompletion.create(
                api_key=api_key, messages=session.messages, **self.compose_args()
            )
            # logger.info("[ChatGPT] reply={}, total_tokens={}".format(response.choices[0]['message']['content'], response["usage"]["total_tokens"]))
            return {"total_tokens": response["usage"]["total_tokens"],
                    "completion_tokens": response["usage"]["completion_tokens"],
                    "content": response.choices[0]['message']['content']}
        except Exception as e:
            need_retry = retry_count < 2
            result = {"completion_tokens": 0, "content": "我现在有点累了，等会再来吧"}
            if isinstance(e, openai.error.RateLimitError):
                logger.warn("[CHATGPT] RateLimitError: {}".format(e))
                result['content'] = "提问太快啦，请休息一下再问我吧"
                if need_retry:
                    time.sleep(5)
            elif isinstance(e, openai.error.Timeout):
                logger.warn("[CHATGPT] Timeout: {}".format(e))
                result['content'] = "我没有收到你的消息"
                if need_retry:
                    time.sleep(5)
            elif isinstance(e, openai.error.APIConnectionError):
                logger.warn("[CHATGPT] APIConnectionError: {}".format(e))
                need_retry = False
                result['content'] = "我连接不到你的网络"
            else:
                logger.warn("[CHATGPT] Exception: {}".format(e))
                need_retry = False
                self.sessions.clear_session(session_id)

            if need_retry:
                logger.warn("[CHATGPT] 第{}次重试".format(retry_count+1))
                return self.reply_text(session, session_id, api_key, retry_count+1)
            else:
                return result


class AzureChatGPTBot(ChatGPTBot):
    def __init__(self):
        super().__init__()
        openai.api_type = "azure"
        openai.api_version = "2023-03-15-preview"

    def compose_args(self):
        args = super().compose_args()
        args["engine"] = args["model"]
        del(args["model"])
        return args
