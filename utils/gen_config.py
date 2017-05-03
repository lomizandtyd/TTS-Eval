import os
import sys

if __name__ == "__main__":
    
    static_dir = './static'
    if len(sys.argv) > 1:
        static_url = sys.argv[1]
    data_dir = os.path.join(static_dir, 'data')
    json_str = "var config = "
    json_data = {"baseurl":data_dir, "exps":[]}
    
    for exp in os.listdir(data_dir):
        exp_dic = {"path":exp}
        exp_dic["styles"] = []
        exp_dic["info"] = ""
        exp_path = os.path.join(data_dir, exp)
        ###
        if exp[:4] == "sMOS":
            for stl in os.listdir(exp_path):
                if stl != "standard":
                    exp_dic["styles"].append(stl)
        else:
            for stl in os.listdir(exp_path):
                exp_dic["styles"].append(stl)
        ###

        ###
        if(exp[:3] == "ABX" or exp[:3] == "MOS" or exp[:4] == "sMOS"):
            if exp[:4] != "sMOS":
                exp_dic["type"] = exp[:3]
            else:
                exp_dic["type"] = "sMOS"
            exp_dic["files"] = []
            style = exp_dic["styles"][0]
            file_path = os.path.join(exp_path,style)
            for fnm in os.listdir(file_path):
                exp_dic["files"].append(fnm)
        elif(exp[:2] == "CM"):
            exp_dic["type"] = "CM"
            exp_dic["files"] = []
            for stl in exp_dic["styles"]:
                file_path = os.path.join(exp_path,stl)
                for fnm in os.listdir(file_path):
                    exp_dic["files"].append(stl + "/" + fnm)
        elif(exp[:4] == "rABX"):
            exp_dic["type"] = "rABX"
            exp_dic["files"] = []
            for stl in exp_dic["styles"]:
                file_path = os.path.join(exp_path,stl)
                tmp_lst = []
                for fnm in os.listdir(file_path):
                    tmp_lst.append("data/" + exp + "/" + stl + "/" + fnm)
                exp_dic["files"].append(tmp_lst)
        else:
            pass
        ###
        json_data["exps"].append(exp_dic)

    json_str += str(json_data) + ";"
    json_path = os.path.join(static_dir, 'scripts/config.js')

    handle = open(json_path, "w")
    handle.write(json_str)
    handle.close()
