from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='vizwiz',
                       karpathy_json_path='data/dataset_viz.json',
                       image_folder='data/vizwiz_imgs/',
                       captions_per_image=5,
                       min_word_freq=3,
                       output_folder='data/vizwiz_captions/',
                       max_len=150)
