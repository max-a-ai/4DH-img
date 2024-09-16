from .vit import vit, vit_small, vit_base, vit_large

def create_backbone(cfg):
    if cfg.MODEL.BACKBONE.TYPE == 'vit':
        return vit(cfg)
    elif cfg.MODEL.BACKBONE.TYPE == 'vit_small':
        return vit_small(cfg)
    elif cfg.MODEL.BACKBONE.TYPE == 'vit_base':
        return vit_base(cfg)
    elif cfg.MODEL.BACKBONE.TYPE == 'vit_large':
        return vit_large(cfg)
    else:
        raise NotImplementedError('Backbone type is not implemented')
