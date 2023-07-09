from bardapi import Bard

token = 'YQgsSmSElC_B71tR3WuRir_0uTO7cQexTvAJPXBJINi7-uhypu0b7nuKKmFpMnlv_cZy7Q.'
bard = Bard(token=token)
print(bard.get_answer("Explain me ChatGPT")['content'])