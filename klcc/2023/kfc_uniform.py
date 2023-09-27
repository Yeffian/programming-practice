start=['d61cea','c1aa7d','aa4e05','e3cf3a','b0789b','ef5780','bcf427','68f994','697728','c3de70','31dc8d','d4ccdb','448525','f4533b','18ae01','a33fba','d18c52','ab81a2','328fc5','1afb05','b1bbb3','61c896','d43799','d56a8a','7f075d','c1e35b','e42fda','de681b','a614ce','c4d074','925e5e','df9a09','b26d10','1809e8','ce0efb','f6f487','b39402','66ffd1','e42113','83aed6','4ed93b','6cf39b','b635b','f08549','e756a','ab9ec9','a76663','f9d6c0','5543e8','edc4d3','595fef','4fc772','2ab63f','55c321','9b1018','cf4f1c','a0d32b','5e0837','8ed602','aa9a7c','7911b2','4be5c4','d9e5b0','5b6386','834ed4','47d9d7','75c83d','606343','74eccb','751515','72df0','1b3f4d','18cb7f','888a8','dcb1a7','479056','76df41','d4b27a','80f8ac','8dc8e7','eab6a1','b8907c','878494','42afa1','a1aa4e','21767a','b7f4dc','6f407b','17cc9b','1c1dc8','9a9e8a','187d9','f4b479','430f29','a8cf9','aef042','2a0c00','4092e2','42636c','b9feff']
end=['23965c','2c8de7','b79910','72c775','63f4d','7cdc28','cb36ee','83160e','8fe1bb','a442fc','6d0b4d','40dfc2','2b374b','ac693b','795415','4e8aa5','feff71','9f8a9e','64b049','d08a0','f60dcd','7a3434','18c88b','f9dc12','4fe3d','5e19b9','4c2d1a','c70f9c','c07c6b','6e7910','ddc047','a7945a','b5556d','ad4b9','bbc46a','56a9','38ee86','ee38a9','b0778f','6de091','6a3a9f','703b85','61a640','5ae6ae','a61c93','a6d80e','7261e0','8566ed','7c04dc','ad88d7','5fde60','2aefab','63bb80','853a65','19a3c6','a068e3','baeda1','bc7efb','bc332c','58a504','4d83bf','19130f','f0d6d5','51cb79','d7482e','e2d018','b4d522','1aebd8','568312','3db0d4','58125b','bec58b','7b7df','92f3b7','2d4228','96177d','96d7c8','384ec5','60a821','b901df','3e6040','f29e07','648809','7a71cb','133b38','afb3ce','5d6455','2ddb7e','c38d3d','c5829','1b8fd4','257d45','c94e1c','ca5c63','5f99c0','439d92','669b81','6337ac','aa3c18','fd4fd5']

diffs=[]

for i in range(len(start)):
    start_d=int(start[i],16)
    end_d=int(end[i],16)
    diff=start_d-end_d
    diffs.append(diff)

print(sum(diffs) // 86400)