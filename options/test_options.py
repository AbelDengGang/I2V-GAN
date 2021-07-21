from .base_options import BaseOptions

# class TestOptions(BaseOptions):
#     def initialize(self):
#         BaseOptions.initialize(self)
#         self.parser.add_argument('--ntest', type=int, default=float("inf"), help='# of test examples.')
#         self.parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')
#         self.parser.add_argument('--aspect_ratio', type=float, default=1.0, help='aspect ratio of result images')
#         self.parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
#         self.parser.add_argument('--which_epoch', type=str, default='latest', help='which epoch to load? set to latest to use latest cached model')
#         self.parser.add_argument('--how_many', type=int, default=50, help='how many test images to run')
#         #self.parser.add_argument('--identity', type=float, default=0.0, help='use identity mapping. Setting identity other than 1 has an effect of scaling the weight of the identity mapping loss. For example, if the weight of the identity loss should be 10 times smaller than the weight of the reconstruction loss, please set optidentity = 0.1')
#         self.isTrain = False


# class TestOptions(BaseOptions):
#     def initialize(self):
#         BaseOptions.initialize(self)
#         self.parser.add_argument('--ntest', type=int, default=float("inf"), help='# of test examples.')
#         self.parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')
#         self.parser.add_argument('--aspect_ratio', type=float, default=1.0, help='aspect ratio of result images')
#         self.parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
#         self.parser.add_argument('--which_epoch', type=str, default='latest', help='which epoch to load? set to latest to use latest cached model')
#         self.parser.add_argument('--how_many', type=int, default=50, help='how many test images to run')
#         self.parser.add_argument('--netF', type=str, default='mlp_sample', choices=['sample', 'reshape', 'mlp_sample'], help='how to downsample the feature map')
#         self.parser.add_argument('--netF_nc', type=int, default=256)
#         self.parser.add_argument('--init_gain', type=float, default=0.02, help='scaling factor for normal, xavier and orthogonal.')
#         self.parser.add_argument('--no_antialias',default=True, action='store_true', help='if specified, use stride=2 convs instead of antialiased-downsampling (sad)')
#         # self.parser.add_argument('--no_antialias', action='store_true', help='if specified, use stride=2 convs instead of antialiased-downsampling (sad)')
#         self.parser.add_argument('--batch_size', type=int, default=1, help='input batch size')
#         self.parser.add_argument('--gpu', type=str, default='0', help='input batch size')
#         self.parser.add_argument('--nce_T', type=float, default=0.07, help='temperature for NCE loss')
#         self.parser.add_argument('--exter_NCE', type=float, default=0.1, help='temperature for exter_NCE loss')
#         self.parser.add_argument('--inter_NCE', type=float, default=1.0, help='temperature for inter_NCE loss')
#         self.parser.add_argument('--identity', type=float, default=0.5, help='use identity mapping. Setting identity other than 1 has an effect of scaling the weight of the identity mapping loss. For example, if the weight of the identity loss should be 10 times smaller than the weight of the reconstruction loss, please set optidentity = 0.1')
#         self.parser.add_argument('--nce_layers', type=str, default='0,4,8,12,16', help='compute NCE loss on which layers')
#         self.parser.add_argument('--num_patches', type=int, default=256, help='number of patches per layer')
#         self.parser.add_argument('--display_env', type=str, default='Traffic', help='visdom display environment name (default is "main")')
#         self.parser.add_argument('--no_antialias_up',  action='store_true', help='if specified, use [upconv(learned filter)] instead of [upconv(hard-coded [1,3,3,1] filter), conv]')
#         #self.parser.add_argument('--identity', type=float, default=0.0, help='use identity mapping. Setting identity other than 1 has an effect of scaling the weight of the identity mapping loss. For example, if the weight of the identity loss should be 10 times smaller than the weight of the reconstruction loss, please set optidentity = 0.1')
#         self.isTrain = False

class TestOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        self.parser.add_argument('--display_freq', type=int, default=100, help='frequency of showing training results on screen')
        self.parser.add_argument('--display_single_pane_ncols', type=int, default=0, help='if positive, display all images in a single visdom web panel with certain number of images per row.')
        self.parser.add_argument('--update_html_freq', type=int, default=1000, help='frequency of saving training results to html')
        self.parser.add_argument('--print_freq', type=int, default=100, help='frequency of showing training results on console')
        self.parser.add_argument('--save_latest_freq', type=int, default=2000, help='frequency of saving the latest results')
        self.parser.add_argument('--save_epoch_freq', type=int, default=5, help='frequency of saving checkpoints at the end of epochs')
        self.parser.add_argument('--continue_train', action='store_true', help='continue training: load the latest model')
        self.parser.add_argument('--epoch_count', type=int, default=1, help='the starting epoch count, we save the model by <epoch_count>, <epoch_count>+<save_latest_freq>, ...')
        self.parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
        self.parser.add_argument('--which_epoch', type=str, default='latest', help='which epoch to load? set to latest to use latest cached model')
        self.parser.add_argument('--niter', type=int, default=35, help='# of iter at starting learning rate')
        self.parser.add_argument('--niter_decay', type=int, default=35, help='# of iter to linearly decay learning rate to zero')
        self.parser.add_argument('--beta1', type=float, default=0.5, help='momentum term of adam')
        self.parser.add_argument('--how_many', type=int, default=-1, help='how many test images to run')
        self.parser.add_argument('--lr', type=float, default=0.0002, help='initial learning rate for adam')
        self.parser.add_argument('--no_lsgan', action='store_true', help='do *not* use least square GAN, if false, use vanilla GAN')
        self.parser.add_argument('--lambda_A', type=float, default=10.0, help='weight for cycle loss (A -> B -> A)')
        self.parser.add_argument('--lambda_B', type=float, default=10.0, help='weight for cycle loss (B -> A -> B)')
        self.parser.add_argument('--pool_size', type=int, default=50, help='the size of image buffer that stores previously generated images')
        self.parser.add_argument('--no_html', action='store_true', help='do not save intermediate training results to [opt.checkpoints_dir]/[opt.name]/web/')
        self.parser.add_argument('--lr_policy', type=str, default='lambda', help='learning rate policy: lambda|step|plateau')
        self.parser.add_argument('--lr_decay_iters', type=int, default=50, help='multiply by a gamma every lr_decay_iters iterations')
        self.parser.add_argument('--identity', type=float, default=0.5, help='use identity mapping. Setting identity other than 1 has an effect of scaling the weight of the identity mapping loss. For example, if the weight of the identity loss should be 10 times smaller than the weight of the reconstruction loss, please set optidentity = 0.1')
        self.parser.add_argument('--nce_layers', type=str, default='0,4,8,12,16', help='compute NCE loss on which layers')
        self.parser.add_argument('--num_patches', type=int, default=256, help='number of patches per layer')
        self.parser.add_argument('--netF', type=str, default='mlp_sample', choices=['sample', 'reshape', 'mlp_sample'], help='how to downsample the feature map')
        self.parser.add_argument('--netF_nc', type=int, default=256)
        self.parser.add_argument('--init_gain', type=float, default=0.02, help='scaling factor for normal, xavier and orthogonal.')
        self.parser.add_argument('--no_antialias',default=True, action='store_true', help='if specified, use stride=2 convs instead of antialiased-downsampling (sad)')
        # self.parser.add_argument('--no_antialias', action='store_true', help='if specified, use stride=2 convs instead of antialiased-downsampling (sad)')
        self.parser.add_argument('--batch_size', type=int, default=1, help='input batch size')
        self.parser.add_argument('--gpu', type=str, default='0', help='input batch size')
        self.parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')
        self.parser.add_argument('--nce_T', type=float, default=0.07, help='temperature for NCE loss')
        self.parser.add_argument('--exter_NCE', type=float, default=0.1, help='temperature for exter_NCE loss')
        self.parser.add_argument('--inter_NCE', type=float, default=1.0, help='temperature for inter_NCE loss')
        self.parser.add_argument('--txtname', type=str, default='InsLoss.txt')
        self.parser.add_argument('--display_env', type=str, default='Traffic', help='visdom display environment name (default is "main")')
        self.parser.add_argument('--no_antialias_up',  action='store_true', help='if specified, use [upconv(learned filter)] instead of [upconv(hard-coded [1,3,3,1] filter), conv]')
        self.isTrain = False