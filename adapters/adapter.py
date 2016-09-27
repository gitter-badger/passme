# -*- coding: utf-8 -*-


import logging
import requests


class Adapter():

    def __init__(self):
        self.auth_url=''
        self._init_logger()

    def check(self,user,passwd):
        checked_status=[0,'nothing happend']
        self.estimate(checked_status)
        return checked_status

    def estimate(self,checked_status):
        if checked_status[0]==0:
            self.logger.warn(checked_status[1])
        if checked_status[0]==-1:
            self.logger.error(checked_status[1])

    def post(self,post,url=False,headers={}):
        if (url==False):
            url=self.auth_url

        sess=requests.Session()
        return sess.post(url,data=post,headers=headers)

    def get(self,url=False,headers={}):
        if (url==False):
            url=self.auth_url
        sess=requests.Session()
        return sess.get(url,headers=headers)


    def _init_logger(self):

        logger = logging.getLogger("passme")
        logging.basicConfig(level=logging.WARNING)
        logger.setLevel(logging.WARN)

        # # create console handler and set level to debug
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.DEBUG)
        # # create formatter
        # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # # add formatter to ch
        # ch.setFormatter(formatter)
        # # add ch to logger
        # logger.addHandler(ch)
        self.logger=logger
