"""Pydantic models for VicEmergency GeoJSON feed."""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class CAPInfo(BaseModel):
    """Common Alerting Protocol information."""
    
    category: Optional[str] = None
    event: Optional[str] = None
    eventCode: Optional[str] = None
    urgency: Optional[str] = None
    severity: Optional[str] = None
    certainty: Optional[str] = None
    contact: Optional[str] = None
    senderName: Optional[str] = None
    responseType: Optional[str] = None


class FeatureProperties(BaseModel):
    """Properties of a GeoJSON feature."""
    
    feedType: str
    sourceOrg: str
    sourceId: Union[str, int]  # Can be string or int
    sourceFeed: str
    sourceTitle: Optional[str] = None
    id: Union[str, int]  # Can be string or int
    category1: Optional[str] = None
    category2: Optional[str] = None
    status: Optional[str] = None
    name: Optional[str] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None  # Some features may not have this
    location: Optional[str] = None
    size: Optional[Union[float, str]] = None  # Can be numeric or "Small", etc
    sizeFmt: Optional[str] = None
    url: Optional[str] = None
    webHeadline: Optional[str] = None
    webBody: Optional[str] = None
    text: Optional[str] = None
    resources: Optional[Union[List[str], int]] = None  # Can be list or count
    mfbId: Optional[Union[str, int]] = None
    cfaId: Optional[Union[str, int]] = None
    eventId: Optional[Union[str, int]] = None
    action: Optional[str] = None
    statewide: Optional[str] = None
    cap: Optional[CAPInfo] = None
    incidentFeatures: Optional[List[Any]] = None  # Nested features
    
    class Config:
        extra = "allow"  # Allow additional fields


class Geometry(BaseModel):
    """GeoJSON geometry."""
    
    type: str
    coordinates: Optional[Union[List[float], List[List[float]], List[List[List[float]]]]] = None
    geometries: Optional[List[Dict[str, Any]]] = None  # For GeometryCollection
    
    class Config:
        extra = "allow"


class Feature(BaseModel):
    """GeoJSON feature."""
    
    type: str = Field(default="Feature")
    properties: FeatureProperties
    geometry: Optional[Geometry] = None


class FeedProperties(BaseModel):
    """Top-level feed properties."""
    
    generated: Optional[datetime] = None
    lastUpdated: Optional[datetime] = None
    authority: Optional[str] = None
    conditions: Optional[Dict[str, Any]] = None
    forecast: Optional[Dict[str, Any]] = None
    featureCount: Optional[int] = None
    
    class Config:
        extra = "allow"


class GeoJSONFeed(BaseModel):
    """Complete GeoJSON feed."""
    
    type: str = Field(default="FeatureCollection")
    features: List[Feature]
    properties: Optional[FeedProperties] = None
    notices: Optional[List[Any]] = None
    lastUpdated: Optional[datetime] = None
    featureCount: Optional[int] = None