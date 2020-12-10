import os
import ffmpy
#import speechEmotionRecognition as sp



def converter():
	inputdir = os.path.abspath(os.getcwd()) + "/input1"
	outdir =  os.path.abspath(os.getcwd()) + "/input"
	print(inputdir)

	for filename in os.listdir(inputdir):
		actual_filename = filename[:-4]
		outputdir_final = os.path.join(outdir, actual_filename)
		try:
			os.mkdir(outputdir_final)
		except OSError:
			print ("Creation of the directory %s failed" % outputdir_final)
		else:
			print ("Successfully created the directory %s " % outputdir_final)
		if(filename.endswith(".mp4")):
			os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}/{}.wav'.format(os.path.join(inputdir, filename), outputdir_final, actual_filename))
			#os.remove(os.path.join(inputdir, filename))
			#sp.init()
		else:
			continue
	

