cd /home/ramaka02/projects/2018/ian/nature_revision_H3K27me3_Suz12_chip/rmdup

nohup macs2 callpeak -t post_differentiation_H3K27me3.merged.bam \
-c ./2017_IanMaze_HistoneSerotonylation_Processed_input_samples/input.merged.bam -f BAM -g 2e9 \
-n ../macs/post_differentiation_H3K27me3_peaks \
--bw 150 -q 0.05 2> ../macs/post_differentiation_H3K27me3 --tempdir /home/ramaka02/tmp &

nohup macs2 callpeak -t post_differentiation_Suz12.merged.bam \
-c ./2017_IanMaze_HistoneSerotonylation_Processed_input_samples/input.merged.bam -f BAM -g 2e9 \
-n ../macs/post_differentiation_Suz12_peaks \
--bw 150 -q 0.05 2> ../macs/post_differentiation_Suz12 --tempdir /home/ramaka02/tmp &

nohup macs2 callpeak -t pre_differentiation_H3K27me3.merged.bam \
-c ./2017_IanMaze_HistoneSerotonylation_Processed_input_samples/input.merged.bam -f BAM -g 2e9 \
-n ../macs/pre_differentiation_H3K27me3_peaks \
--bw 150 -q 0.05 2> ../macs/pre_differentiation_H3K27me3 --tempdir /home/ramaka02/tmp &

nohup macs2 callpeak -t pre_differentiation_Suz12.merged.bam \
-c ./2017_IanMaze_HistoneSerotonylation_Processed_input_samples/input.merged.bam -f BAM -g 2e9 \
-n ../macs/pre_differentiation_Suz12_peaks \
--bw 150 -q 0.05 2> ../macs/pre_differentiation_Suz12 --tempdir /home/ramaka02/tmp &

