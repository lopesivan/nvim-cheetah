# -*- coding: utf-8 -*-

try:
    import sys
    import vim
    import os
    import glob
    from Cheetah.Template import Template

    curpath = vim.eval("$HOME")
    sys.path = [curpath+"/.config/nvim/site/pack/packer/start/nvim-cheetah/plugin"] + sys.path

    import cheetah
    import yaml

    def cheetahPythonInput(message='input'):
        vim.command('call inputsave()')
        vim.command("let user_input = input('" + message + ": ')")
        vim.command('call inputrestore()')
        #print('{} {}'.format('before:', message))
        return vim.eval('user_input')

    def cheetahMainTemplate():

        YML = "{}/{}".format(vim.eval('expand("%:p:h")'), "cheetah.yml")
        for f in glob.glob(YML):
            # print('{} {}'.format('file  :', f))
            config_file = open(f, 'r')
            #TODO: 🐱    >  YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the defaul t Loader is unsafe. Please read https://msg.pyyaml.org/load for full details.
            #data_model = yaml.load(config_file)
            data_model = yaml.load(config_file, Loader=yaml.FullLoader)
            config_file.close()

            type_name = data_model['type']
            template_name = data_model['cheetah']
            view = os.path.expandvars("$HOME/.config/nvim/cheetah/"+type_name+"/"+template_name+".cheetah")

            if os.path.isfile(view):

                dataout = Template(open(view).read(),
                                   searchList=[{'d': data_model}])

                buffer = vim.current.window.buffer
                cheetah.Redirect(buffer)
                print(dataout)

                # To redirect output back just do
                sys.stdout = sys._stdout

                # number_of_lines = len(buffer)
                # print('{} {}'.format('after :', number_of_lines))

                # delete two last lines
                del buffer[-1]
                del buffer[-1]

                # number_of_lines = len(buffer)
                # print('{} {}'.format('before:', number_of_lines))
            else:
                print("File not found:" + view)

except ImportError as e:
    print("Package not installed, please run: pip install cheetah")
