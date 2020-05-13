#!/usr/bin/python
#coding: utf-8


from redis import StrictRedis
import click


@click.command()
@click.option("--src_host", "-sh",default="127.0.0.1",help="source ip address")
@click.option("--src_port", "-st",default=6379, help="source host port")
@click.option("--src_db", "-sdb",default=0, help="source host db 0-15")
@click.option("--src_passwd","-sp", default="", help="source host auth password")
@click.option("--dest_host", "-dh",default="127.0.0.1", help="dest ip address")
@click.option("--dest_port", "-dt",default=6379, help="dest host port")
@click.option("--dest_db", "-ddb",default=0, help="dest host db 0-15")
@click.option("--dest_passwd", "-dp",default="", help="dest host auth password")
def redis_sync(src_host,src_port,src_db,src_passwd,dest_host,dest_port,dest_db,dest_passwd):
    r1 = StrictRedis(host=src_host,port=src_port, db=src_db, password=src_passwd)
    r2 = StrictRedis(host=dest_host,port=dest_port, db=dest_db, password=dest_passwd)

    keys = r1.keys("*")

    for k in keys:
        s = r1.type(k)
        if s.decode() == "string":
            val = r1.get(k)
            r2.set(k,val)
        elif s.decode() == "list":
            llist = r1.lrange(k,0,-1)
            for i in range(len(llist)):
                r2.rpush(k,llist[i])
        elif s.decode() == "hash":
            val = r1.hgetall(k)
            for k1,v in val.items():
                r2.hset(name=k,key=k1,value=v)
        elif s.decode() == "set":
            lset = r1.smembers(k)
            r2.sadd(k,*lset)


if __name__ == "__main__":
    redis_sync()
