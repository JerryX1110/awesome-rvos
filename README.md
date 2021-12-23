# Awesome-Referring-Video-Object-Segmentation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Welcome to starts ⭐ & comments 💹 & collaboration 😀 !!

```diff
- 2021.12.23: Add scripts to prepare ALL the datasets needed automatically!
- 2021.12.12: Recent papers (from 2021) 
- welcome to add if any information misses. 😎
```

---

## Introduction

![image](https://user-images.githubusercontent.com/65257938/145671552-f3d3dad7-77e4-4f12-98de-016cc1184976.png)

**Referring video object segmentation** aims at **segmenting an object in video with language expressions**. 

Unlike the previous video object segmentation, the task exploits a different type of supervision, language expressions, **to identify and segment an object referred by the given language expressions in a video**. A detailed explanation of the new task can be found in the following paper.

Seonguk Seo, Joon-Young Lee, Bohyung Han, “URVOS: Unified Referring Video Object Segmentation Network with a Large-Scale Benchmark”, European Conference on Computer Vision (ECCV), 2020:<https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123600205.pdf>

## Impressive Works Related to Referring Video Object Segmentation (RVOS)

1.**MTTR**:<https://github.com/mttr2021/MTTR>
![image](https://user-images.githubusercontent.com/65257938/145671132-1a2c014e-6563-4f2e-91bd-cd58ed999a0a.png)


2.**PMINet**:<https://youtube-vos.org/assets/challenge/2021/reports/RVOS_2_Ding.pdf>
![image](https://user-images.githubusercontent.com/65257938/145671186-0515bf89-1d71-4155-b3f9-27d6903e3f31.png)


3.**CMPC-V [PAMI 2021]**:<https://github.com/spyflying/CMPC-Refseg>

Cross-modal progressive comprehension for referring segmentation:<https://arxiv.org/abs/2105.07175>
![image](https://user-images.githubusercontent.com/65257938/145671302-40924570-9cd2-4ffa-84d3-5bd11b95358d.png)

4.**URVOS [ECCV 2020]**:<https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123600205.pdf>
![image](https://user-images.githubusercontent.com/65257938/145671358-229d8e56-8d40-4cc1-bb4f-58bbff38a452.png)


## Benchmark
[The 3rd Large-scale Video Object Segmentation - Track 3: Referring Video Object Segmentation](https://competitions.codalab.org/competitions/29139#results)

[Download_DATA](https://drive.google.com/drive/folders/1J45ubR8Y24wQ6dzKOTkfpd9GS_F9A2kb)

## Related Datasets
* **YouTube-VOS**:
```shell
wget https://github.com/JerryX1110/awesome-rvos/blob/main/down_YTVOS_w_refer.py
python down_YTVOS_w_refer.py
```

Folder structure:
```latex
data/
└── refer_youtube_vos/ 
    ├── train/
    │   ├── JPEGImages/
    │   │   └── */ (video folders)
    │   │       └── *.jpg (frame image files) 
    │   └── Annotations/
    │       └── */ (video folders)
    │           └── *.png (mask annotation files) 
    ├── valid/
    │   └── JPEGImages/
    │       └── */ (video folders)
    │           └── *.jpg (frame image files) 
    └── meta_expressions/
        ├── train/
        │   └── meta_expressions.json  (text annotations)
        └── valid/
            └── meta_expressions.json  (text annotations)
```



* **A2D-Sentences**:

REPO:<https://web.eecs.umich.edu/~jjcorso/r/a2d/>

paper:<https://arxiv.org/abs/1803.07485>

![image](https://user-images.githubusercontent.com/65257938/147182456-d4f25e64-a8a0-4e18-9d56-8bbdacae6f80.png)

Citation:
```latex
@misc{gavrilyuk2018actor,
      title={Actor and Action Video Segmentation from a Sentence}, 
      author={Kirill Gavrilyuk and Amir Ghodrati and Zhenyang Li and Cees G. M. Snoek},
      year={2018},
      eprint={1803.07485},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
License: The dataset may not be republished in any form without the written consent of the authors.

[README](https://web.eecs.umich.edu/~jjcorso/r/a2d/files/README)
Dataset and Annotation (version 1.0, 1.9GB, [tar.bz](https://web.eecs.umich.edu/~jjcorso/bigshare/A2D_main_1_0.tar.bz))
Evaluation Toolkit (version 1.0, [tar.bz](https://web.eecs.umich.edu/~jjcorso/bigshare/A2D_eval_1_0.tar.bz))

```shell
mkdir a2d_sentences
cd a2d_sentences
wget https://web.eecs.umich.edu/~jjcorso/bigshare/A2D_main_1_0.tar.bz
tar jxvf A2D_main_1_0.tar.bz
mkdir text_annotations

cd text_annotations
wget https://kgavrilyuk.github.io/actor_action/a2d_annotation.txt
wget https://kgavrilyuk.github.io/actor_action/a2d_missed_videos.txt
wget https://github.com/JerryX1110/awesome-rvos/blob/main/down_a2d_annotation_with_instances.py
python down_a2d_annotation_with_instances.py
unzip a2d_annotation_with_instances.zip
#rm a2d_annotation_with_instances.zip
cd ..

cd ..

```




Folder structure:
```latex
data/
└── a2d_sentences/ 
    ├── Release/
    │   ├── videoset.csv  (videos metadata file)
    │   └── CLIPS320/
    │       └── *.mp4     (video files)
    └── text_annotations/
        ├── a2d_annotation.txt  (actual text annotations)
        ├── a2d_missed_videos.txt
        └── a2d_annotation_with_instances/ 
            └── */ (video folders)
                └── *.h5 (annotations files) 
```

Citation:
```latex
@inproceedings{YaXuCaCVPR2017,
  author = {Yan, Y. and Xu, C. and Cai, D. and {\bf Corso}, {\bf J. J.}},
  booktitle = {{Proceedings of IEEE Conference on Computer Vision and Pattern Recognition}},
  tags = {computer vision, activity recognition, video understanding, semantic segmentation},
  title = {Weakly Supervised Actor-Action Segmentation via Robust Multi-Task Ranking},
  year = {2017}
}
@inproceedings{XuCoCVPR2016,
  author = {Xu, C. and {\bf Corso}, {\bf J. J.}},
  booktitle = {{Proceedings of IEEE Conference on Computer Vision and Pattern Recognition}},
  datadownload = {http://web.eecs.umich.edu/~jjcorso/r/a2d},
  tags = {computer vision, activity recognition, video understanding, semantic segmentation},
  title = {Actor-Action Semantic Segmentation with Grouping-Process Models},
  year = {2016}
}
@inproceedings{XuHsXiCVPR2015,
  author = {Xu, C. and Hsieh, S.-H. and Xiong, C. and {\bf Corso}, {\bf J. J.}},
  booktitle = {{Proceedings of IEEE Conference on Computer Vision and Pattern Recognition}},
  datadownload = {http://web.eecs.umich.edu/~jjcorso/r/a2d},
  poster = {http://web.eecs.umich.edu/~jjcorso/pubs/xu_corso_CVPR2015_A2D_poster.pdf},
  tags = {computer vision, activity recognition, video understanding, semantic segmentation},
  title = {Can Humans Fly? {Action} Understanding with Multiple Classes of Actors},
  url = {http://web.eecs.umich.edu/~jjcorso/pubs/xu_corso_CVPR2015_A2D.pdf},
  year = {2015}
}
```

* **J-HMDB**:<http://jhmdb.is.tue.mpg.de/>

![image](https://user-images.githubusercontent.com/65257938/147182575-9ee87a7d-c78d-4ce8-90fe-1109204643da.png)

downloading_script
```shell
mkdir jhmdb_sentences
cd jhmdb_sentences
wget http://files.is.tue.mpg.de/jhmdb/Rename_Images.tar.gz
wget https://kgavrilyuk.github.io/actor_action/jhmdb_annotation.txt
wget http://files.is.tue.mpg.de/jhmdb/puppet_mask.zip
tar -xzvf  Rename_Images.tar.gz
unzip puppet_mask.zip
cd ..
```

Folder structure:
```latex
data/
└── jhmdb_sentences/ 
    ├── Rename_Images/  (frame images)
    │   └── */ (action dirs)
    ├── puppet_mask/  (mask annotations)
    │   └── */ (action dirs)
    └── jhmdb_annotation.txt  (text annotations)
```

Citation:
```latex
@inproceedings{Jhuang:ICCV:2013,
title = {Towards understanding action recognition},
author = {H. Jhuang and J. Gall and S. Zuffi and C. Schmid and M. J. Black},
booktitle = {International Conf. on Computer Vision (ICCV)},
month = Dec,
pages = {3192-3199},
year = {2013}
}
```

## Other related datasets
### Image Grounding Datasets

1. **Flickr30k**: Plummer, Bryan A., et al. **Flickr30k entities: Collecting region-to-phrase correspondences for richer image-to-sentence models.** Proceedings of the IEEE international conference on computer vision. 2015. [[Paper]](https://arxiv.org/abs/1505.04870) [[Code]](https://github.com/BryanPlummer/pl-clc) [[Website]](http://web.engr.illinois.edu/~bplumme2/Flickr30kEntities/)

1. **RefClef**: Kazemzadeh, Sahar, et al. **Referitgame: Referring to objects in photographs of natural scenes.** Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP). 2014. [[Paper]](http://www.aclweb.org/anthology/D14-1086) [[Website]](http://tamaraberg.com/referitgame/)

1. **RefCOCOg**: Mao, Junhua, et al. **Generation and comprehension of unambiguous object descriptions.** Proceedings of the IEEE conference on computer vision and pattern recognition. 2016. [[Paper]](https://arxiv.org/pdf/1511.02283.pdf) [[Code]](https://github.com/mjhucla/Google_Refexp_toolbox)

1. **RefCOCO and RefCOCO+**: 1. Yu, Licheng, et al. **Modeling context in referring expressions.** European Conference on Computer Vision. Springer, Cham, 2016. [[Paper]](https://arxiv.org/pdf/1608.00272.pdf)[[Code]](https://github.com/lichengunc/refer)

1. **Visual Genome**: Krishna, Ranjay, et al. **Visual genome: Connecting language and vision using crowdsourced dense image annotations.** International Journal of Computer Vision 123.1 (2017): 32-73. [[Paper]](https://arxiv.org/pdf/1602.07332.pdf) [[Website]](https://visualgenome.org/)

Instructions on RefClef, RefCOCO, RefCOCO+, RefCOCOg is nicely summarized here: https://github.com/lichengunc/refer

### Video Datasets

1. **TaCoS**: Regneri, Michaela, et al. **Grounding action descriptions in videos.** Transactions of the Association of Computational Linguistics 1 (2013): 25-36. [[Paper]](http://aclweb.org/anthology/Q13-1003) [[Website]](http://www.coli.uni-saarland.de/projects/smile/page.php?id=tacos)

1. **Charades**: Sigurdsson, Gunnar A., et al. **Hollywood in homes: Crowdsourcing data collection for activity understanding.** European Conference on Computer Vision. Springer, Cham, 2016. [[Paper]](https://arxiv.org/pdf/1604.01753.pdf) [[Website]](https://allenai.org/plato/charades/)

1. **Charades-STA**: Gao, Jiyang, et al. **Tall: Temporal activity localization via language query.** arXiv preprint arXiv:1705.02101 (2017).[[Paper]](https://arxiv.org/pdf/1705.02101.pdf) [[Code]](https://github.com/jiyanggao/TALL)

1. **Distinct Describable Moments (DiDeMo)**: Hendricks, Lisa Anne, et al. **Localizing moments in video with natural language.** Proceedings of the IEEE International Conference on Computer Vision (ICCV). 2017. *Method name: MCN* [[Paper]](https://arxiv.org/pdf/1708.01641.pdf) [[Code]](https://github.com/LisaAnne/LocalizingMoments) [[Website]](https://people.eecs.berkeley.edu/~lisa_anne/didemo.html)

1. **ActivityNet Captions**: Krishna, Ranjay, et al. **Dense-captioning events in videos.** Proceedings of the IEEE International Conference on Computer Vision. 2017. [[Paper]](https://arxiv.org/pdf/1705.00754.pdf) [[Website]](https://cs.stanford.edu/people/ranjaykrishna/densevid/)

1. **Charades-Ego**:  [[Website]](https://allenai.org/plato/charades/)
	- Sigurdsson, Gunnar, et al. **Actor and Observer: Joint Modeling of First and Third-Person Videos.** CVPR-IEEE Conference on Computer Vision & Pattern Recognition. 2018. [[Paper]](https://arxiv.org/pdf/1804.09627.pdf) [[Code]](https://github.com/gsig/actor-observer)
    - Sigurdsson, Gunnar A., et al. "Charades-Ego: A Large-Scale Dataset of Paired Third and First Person Videos." arXiv preprint arXiv:1804.09626 (2018). [[Paper]](https://arxiv.org/pdf/1804.09626.pdf) [[Code]](https://github.com/gsig/charades-algorithms)
    
1. **TEMPO**: Hendricks, Lisa Anne, et al. **Localizing Moments in Video with Temporal Language.** arXiv preprint arXiv:1809.01337 (2018). [[Paper]](https://arxiv.org/pdf/1809.01337.pdf) [[Code]](https://github.com/LisaAnne/TemporalLanguageRelease) [[Website]](https://people.eecs.berkeley.edu/~lisa_anne/tempo.html)


## Credit
[Awesome Visual Grounding](https://github.com/qy-feng/awesome-visual-grounding)
