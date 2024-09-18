from .vit import vit, vit_small

def create_backbone(cfg):
    if cfg.MODEL.BACKBONE.TYPE == 'vit':
        return vit(cfg)
    elif cfg.MODEL.BACKBONE.TYPE == 'vit_small':
        return vit_small(cfg)
    elif cfg.MODEL.BACKBONE.TYPE == 'vit_base':
        return vit(cfg, 'B')
    elif cfg.MODEL.BACKBONE.TYPE == 'vit_large':
        return vit(cfg, 'L')
    else:
        raise NotImplementedError('Backbone type is not implemented')
