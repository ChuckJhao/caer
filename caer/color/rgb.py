#    _____           ______  _____ 
#  / ____/    /\    |  ____ |  __ \
# | |        /  \   | |__   | |__) | Caer - Modern Computer Vision
# | |       / /\ \  |  __|  |  _  /  Languages: Python, C, C++
# | |___   / ____ \ | |____ | | \ \  http://github.com/jasmcaus/caer
#  \_____\/_/    \_ \______ |_|  \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Caer Authors <http://github.com/jasmcaus>


import cv2 as cv 
import numpy as np 
Tensor = np.ndarray

from .constants import RGB2BGR, RGB2GRAY, RGB2HSV, RGB2LAB, RGB2HLS

__all__ = [
    'rgb_to_bgr',
    'rgb_to_gray',
    'rgb_to_hsv',
    'rgb_to_lab',
    'rgb_to_hls',
    'is_rgb_image',
]

def is_rgb_image(img):
    return len(img.shape) == 3 and img.shape[-1] == 3


def rgb_to_bgr(img) -> Tensor:
    r"""
        Converts an RGB image to its BGR version.

    Args:
        img (ndarray): Valid RGB image array
    
    Returns:
        BGR image array of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not is_rgb_image(img):
        raise ValueError(f'Image of shape 3 expected. Found shape {len(img.shape)}. This method converts an RGB image to its BGR counterpart')

    return cv.cvtColor(img, RGB2BGR)


def rgb_to_gray(img) -> Tensor:
    r"""
        Converts an RGB image to its Grayscale version.

    Args:
        img (ndarray): Valid RGB image array
    
    Returns:
        Grayscale image array of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not is_rgb_image(img):
        raise ValueError(f'Image of shape 3 expected. Found shape {len(img.shape)}. This method converts an RGB image to its Grayscale counterpart')
    
    return cv.cvtColor(img, RGB2GRAY)


def rgb_to_hsv(img) -> Tensor:
    r"""
        Converts an RGB image to its HSV version.

    Args:
        img (ndarray): Valid RGB image array
    
    Returns:
        HSV image array of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not is_rgb_image(img):
        raise ValueError(f'Image of shape 3 expected. Found shape {len(img.shape)}. This method converts an RGB image to its HSV counterpart')
    
    return cv.cvtColor(img, RGB2HSV)


def rgb_to_lab(img) -> Tensor:
    r"""
        Converts an RGB image to its LAB version.

    Args:
        img (ndarray): Valid RGB image array
    
    Returns:
        LAB image array of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not is_rgb_image(img):
        raise ValueError(f'Image of shape 3 expected. Found shape {len(img.shape)}. This method converts an RGB image to its LAB counterpart')

    return cv.cvtColor(img, RGB2LAB)


def rgb_to_hls(img) -> Tensor:
    r"""
        Converts an RGB image to its HLS version.

    Args:
        img (ndarray): Valid RGB image array
    
    Returns:
        HLS image array of shape ``(height, width, channels)``
    
    Raises:
        ValueError: If `img` is not of shape 3
        
    """
    if not is_rgb_image(img):
        raise ValueError(f'Image of shape 3 expected. Found shape {len(img.shape)}. This method converts an RGB image to its HLS counterpart')
    
    return cv.cvtColor(img, RGB2HLS)