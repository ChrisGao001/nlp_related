#-*-coding:utf8-*-

#4-tags for character tagging: B(Begin),E(End),M(Middle),S(Single)

import codecs
import sys
import argparse

reload(sys)
sys.setdefaultencoding("utf8")

def character_tagging(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    for line in input_data:
        word_list = line.strip().split()
        for word in word_list:
            if len(word) == 1:
                output_data.write(word + "\tS\n")
            else:
                output_data.write(word[0] + "\tB\n")
                for w in word[1:len(word)-1]:
                    output_data.write(w + "\tM\n")
                output_data.write(word[len(word)-1] + "\tE\n")
        output_data.write("\n")
    input_data.close()
    output_data.close()
    print('生成训练文件完成！')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("src_path", type=str, help="source path")
    parser.add_argument("dest_path", type=str, help="dest path")
    args = parser.parse_args()
	
    character_tagging(args.src_path, args.dest_path)
